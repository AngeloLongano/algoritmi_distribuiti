window.MkDocsExporter = window.MkDocsExporter || {};

window.MkDocsExporter.render = async () => {
  const isPdfExporter = window.location.protocol === "file:" || !!window.PagedConfig;
  if (!isPdfExporter) {
    return;
  }

  const toRemove = [
    ".navbar",
    ".navbar.fixed-top",
    ".bs-sidebar",
    ".navbar-header",
    ".navbar-toggler",
    ".navbar-collapse",
    ".col-md-3",
    "footer",
  ];

  for (const selector of toRemove) {
    document.querySelectorAll(selector).forEach((el) => el.remove());
  }

  document.body.style.paddingTop = "0";

  if (!window.MathJax) {
    return;
  }

  if (window.MathJax.startup && window.MathJax.startup.promise) {
    await window.MathJax.startup.promise;
  }

  if (typeof window.MathJax.typesetPromise === 'function') {
    await window.MathJax.typesetPromise();
  }
};
