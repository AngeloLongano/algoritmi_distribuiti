document.addEventListener("DOMContentLoaded", function () {
  var toc = document.getElementById("toc-collapse");
  var navbarContainer = document.querySelector(".navbar .container");
  var navToggle = document.querySelector(".navbar .navbar-toggler");
  var tocStorageKey = "mkdocs.toc.hidden";
  var themeStorageKey = "mkdocs.theme.dark";

  function setDarkMode(enabled) {
    document.body.classList.toggle("dark-mode", enabled);
    document.documentElement.setAttribute("data-bs-theme", enabled ? "dark" : "light");
    localStorage.setItem(themeStorageKey, enabled ? "1" : "0");
    var themeIcon = document.querySelector("#theme-toggle-btn i");
    if (themeIcon) {
      themeIcon.className = enabled ? "fa-solid fa-sun" : "fa-solid fa-moon";
    }
  }

  function setTocVisibility(visible) {
    if (!toc) return;
    toc.classList.toggle("show", visible);
    document.body.classList.toggle("toc-hidden", !visible);
    localStorage.setItem(tocStorageKey, visible ? "0" : "1");
    var tocBtn = document.getElementById("toc-toggle-btn");
    if (tocBtn) {
      tocBtn.setAttribute("aria-pressed", visible ? "true" : "false");
      tocBtn.title = visible ? "Nascondi indice" : "Mostra indice";
    }
  }

  function initializeTheme() {
    var storedTheme = localStorage.getItem(themeStorageKey);
    var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    setDarkMode(storedTheme === null ? prefersDark : storedTheme === "1");
  }

  function initializeToc() {
    if (!toc) return;
    var storedToc = localStorage.getItem(tocStorageKey);
    var showToc = storedToc === null ? window.innerWidth >= 992 : storedToc !== "1";
    setTocVisibility(showToc);
    toc.addEventListener("shown.bs.collapse", function () {
      setTocVisibility(true);
    });
    toc.addEventListener("hidden.bs.collapse", function () {
      setTocVisibility(false);
    });
  }

  function mountControls() {
    if (!navbarContainer || !navToggle) return;
    if (document.getElementById("toc-toggle-btn") || document.getElementById("theme-toggle-btn")) return;

    var brand = navbarContainer.querySelector(".navbar-brand");

    var tocBtn = document.createElement("button");
    tocBtn.id = "toc-toggle-btn";
    tocBtn.className = "app-control-btn app-control-btn--toc";
    tocBtn.type = "button";
    tocBtn.title = "Nascondi indice";
    tocBtn.setAttribute("aria-label", "Mostra o nascondi indice");
    tocBtn.setAttribute("aria-pressed", "true");
    tocBtn.innerHTML = '<i class="fa-solid fa-list-ul"></i>';

    if (brand) {
      navbarContainer.insertBefore(tocBtn, brand);
    } else {
      navbarContainer.prepend(tocBtn);
    }

    var controls = document.createElement("div");
    controls.className = "app-controls";
    controls.innerHTML =
      '<button id="theme-toggle-btn" class="app-control-btn" type="button" title="Attiva o disattiva dark mode" aria-label="Attiva o disattiva dark mode"><i class="fa-solid fa-moon"></i></button>';

    navToggle.parentNode.insertBefore(controls, navToggle);

    var themeBtn = document.getElementById("theme-toggle-btn");

    if (tocBtn) {
      tocBtn.addEventListener("click", function () {
        var visible = !document.body.classList.contains("toc-hidden");
        setTocVisibility(!visible);
      });
    }

    if (themeBtn) {
      themeBtn.addEventListener("click", function () {
        setDarkMode(!document.body.classList.contains("dark-mode"));
      });
    }
  }

  mountControls();
  initializeTheme();
  initializeToc();
});
