#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse


MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*]\((?P<dest><[^>\n]+>|[^)\n]+)\)")
OBSIDIAN_IMAGE_RE = re.compile(r"!\[\[(?P<dest>[^\]\n]+)\]\]")


@dataclass
class FileStats:
    copied: int = 0
    updated_refs: int = 0
    normalized_asset_refs: int = 0
    warnings: list[str] = field(default_factory=list)


@dataclass
class FileState:
    md_path: Path
    asset_root: Path
    counter: int = 1
    source_to_new_ref: dict[Path, str] = field(default_factory=dict)

    @property
    def target_dir(self) -> Path:
        return self.asset_root / f"{self.md_path.stem}_images"

    def copy_image(self, source: Path) -> str:
        resolved_source = source.resolve()
        if resolved_source in self.source_to_new_ref:
            return self.source_to_new_ref[resolved_source]

        self.target_dir.mkdir(parents=True, exist_ok=True)
        suffix = resolved_source.suffix

        while True:
            destination = self.target_dir / f"image_{self.counter}{suffix}"
            self.counter += 1
            if not destination.exists():
                break

        shutil.copy2(resolved_source, destination)
        relative_ref = os.path.relpath(destination, self.md_path.parent).replace(os.sep, "/")
        self.source_to_new_ref[resolved_source] = relative_ref
        return relative_ref


def is_remote_reference(value: str) -> bool:
    if re.match(r"^[A-Za-z]:[\\/]", value):
        return False
    parsed = urlparse(value)
    if parsed.scheme:
        return True
    if value.startswith("//"):
        return True
    return False


def split_core_and_trailer(path_ref: str) -> tuple[str, str]:
    for separator in ("?", "#"):
        idx = path_ref.find(separator)
        if idx != -1:
            return path_ref[:idx], path_ref[idx:]
    return path_ref, ""


def resolve_candidate(core_ref: str, md_path: Path, vault_root: Path) -> Path | None:
    if not core_ref:
        return None

    decoded = unquote(core_ref.strip())
    if not decoded:
        return None

    if is_remote_reference(decoded):
        return None

    if decoded.startswith("/"):
        vault_candidate = (vault_root / decoded.lstrip("/")).resolve()
        if vault_candidate.exists():
            return vault_candidate
        absolute_candidate = Path(decoded)
        return absolute_candidate.resolve() if absolute_candidate.exists() else None

    candidate = (md_path.parent / decoded).resolve()
    if candidate.exists():
        return candidate

    return None


def is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def parse_markdown_destination(dest: str) -> tuple[str, str, bool]:
    stripped = dest.strip()
    if stripped.startswith("<"):
        end = stripped.find(">")
        if end != -1:
            return stripped[1:end], stripped[end + 1 :], True

    for idx, char in enumerate(stripped):
        if char.isspace():
            return stripped[:idx], stripped[idx:], False
    return stripped, "", False


def build_markdown_destination(path_ref: str, trailing: str, wrapped: bool) -> str:
    if wrapped:
        return f"<{path_ref}>{trailing}"
    return f"{path_ref}{trailing}"


def parse_obsidian_destination(dest: str) -> tuple[str, str]:
    if "|" in dest:
        head, tail = dest.split("|", 1)
        return head, f"|{tail}"
    return dest, ""


def iter_markdown_replacements(
    text: str, md_path: Path, vault_root: Path, state: FileState, stats: FileStats
) -> Iterable[tuple[int, int, str]]:
    for match in MARKDOWN_IMAGE_RE.finditer(text):
        original_dest = match.group("dest")
        path_ref, trailing, wrapped = parse_markdown_destination(original_dest)
        core_ref, trailer = split_core_and_trailer(path_ref)
        source = resolve_candidate(core_ref, md_path, vault_root)
        if source is None:
            continue
        if is_under(source, state.asset_root):
            continue

        new_ref = state.copy_image(source) + trailer
        new_dest = build_markdown_destination(new_ref, trailing, wrapped)
        dest_start, dest_end = match.span("dest")
        yield dest_start, dest_end, new_dest
        stats.copied = len(state.source_to_new_ref)
        stats.updated_refs += 1


def iter_obsidian_replacements(
    text: str, md_path: Path, vault_root: Path, state: FileState, stats: FileStats
) -> Iterable[tuple[int, int, str]]:
    for match in OBSIDIAN_IMAGE_RE.finditer(text):
        original_dest = match.group("dest")
        path_ref, tail = parse_obsidian_destination(original_dest)
        core_ref, trailer = split_core_and_trailer(path_ref)
        source = resolve_candidate(core_ref, md_path, vault_root)
        if source is None:
            continue
        if is_under(source, state.asset_root):
            continue

        new_ref = state.copy_image(source) + trailer
        new_dest = f"{new_ref}{tail}"
        dest_start, dest_end = match.span("dest")
        yield dest_start, dest_end, new_dest
        stats.copied = len(state.source_to_new_ref)
        stats.updated_refs += 1


def apply_replacements(text: str, replacements: list[tuple[int, int, str]]) -> str:
    updated = text
    for start, end, new_value in sorted(replacements, key=lambda item: item[0], reverse=True):
        updated = f"{updated[:start]}{new_value}{updated[end:]}"
    return updated


def normalize_asset_reference(md_path: Path, source: Path) -> str:
    return os.path.relpath(source, md_path.parent).replace(os.sep, "/")


def process_markdown_file(
    md_path: Path,
    vault_root: Path,
    asset_root: Path,
    normalize_existing_asset_refs: bool,
) -> FileStats:
    stats = FileStats()
    text = md_path.read_text(encoding="utf-8")
    state = FileState(md_path=md_path, asset_root=asset_root)

    replacements = list(iter_markdown_replacements(text, md_path, vault_root, state, stats))
    replacements.extend(iter_obsidian_replacements(text, md_path, vault_root, state, stats))

    if normalize_existing_asset_refs:
        for match in MARKDOWN_IMAGE_RE.finditer(text):
            original_dest = match.group("dest")
            path_ref, trailing, wrapped = parse_markdown_destination(original_dest)
            core_ref, trailer = split_core_and_trailer(path_ref)
            source = resolve_candidate(core_ref, md_path, vault_root)
            if source is None or not is_under(source, asset_root):
                continue

            normalized_ref = normalize_asset_reference(md_path, source) + trailer
            if normalized_ref == path_ref:
                continue

            new_dest = build_markdown_destination(normalized_ref, trailing, wrapped)
            dest_start, dest_end = match.span("dest")
            replacements.append((dest_start, dest_end, new_dest))
            stats.normalized_asset_refs += 1

        for match in OBSIDIAN_IMAGE_RE.finditer(text):
            original_dest = match.group("dest")
            path_ref, tail = parse_obsidian_destination(original_dest)
            core_ref, trailer = split_core_and_trailer(path_ref)
            source = resolve_candidate(core_ref, md_path, vault_root)
            if source is None or not is_under(source, asset_root):
                continue

            normalized_ref = normalize_asset_reference(md_path, source) + trailer
            if normalized_ref == path_ref:
                continue

            new_dest = f"{normalized_ref}{tail}"
            dest_start, dest_end = match.span("dest")
            replacements.append((dest_start, dest_end, new_dest))
            stats.normalized_asset_refs += 1

    if not replacements:
        return stats

    new_text = apply_replacements(text, replacements)
    if new_text != text:
        md_path.write_text(new_text, encoding="utf-8")

    return stats


def run(vault: Path, normalize_existing_asset_refs: bool) -> int:
    vault_root = vault.resolve()
    if not vault_root.exists() or not vault_root.is_dir():
        print(f"Vault non valido: {vault}")
        return 1

    asset_root = vault_root / "assets"
    asset_root.mkdir(parents=True, exist_ok=True)

    md_files = sorted(vault_root.rglob("*.md"))
    total_files = 0
    updated_files = 0
    copied_images = 0
    updated_refs = 0
    normalized_asset_refs = 0

    for md_file in md_files:
        total_files += 1
        stats = process_markdown_file(
            md_file,
            vault_root,
            asset_root,
            normalize_existing_asset_refs=normalize_existing_asset_refs,
        )
        if stats.updated_refs > 0 or stats.normalized_asset_refs > 0:
            updated_files += 1
            copied_images += stats.copied
            updated_refs += stats.updated_refs
            normalized_asset_refs += stats.normalized_asset_refs
            print(
                f"Aggiornato {md_file.relative_to(vault_root)}: "
                f"{stats.updated_refs} riferimenti, "
                f"{stats.normalized_asset_refs} asset normalizzati, "
                f"{stats.copied} immagini copiate"
            )

    print(
        f"Completato. File markdown: {total_files}, file aggiornati: {updated_files}, "
        f"riferimenti aggiornati: {updated_refs}, "
        f"asset normalizzati: {normalized_asset_refs}, "
        f"immagini copiate: {copied_images}"
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Riorganizza le immagini nei markdown di un vault Obsidian."
    )
    parser.add_argument(
        "--vault",
        required=True,
        type=Path,
        help="Percorso della cartella root del vault Obsidian",
    )
    parser.add_argument(
        "--no-normalize-existing-asset-refs",
        action="store_true",
        help=(
            "Non riscrive i riferimenti immagine gia' dentro assets/ in path relativi "
            "(default: li normalizza, utile per Obsidian)."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run(
        args.vault,
        normalize_existing_asset_refs=not args.no_normalize_existing_asset_refs,
    )


if __name__ == "__main__":
    raise SystemExit(main())
