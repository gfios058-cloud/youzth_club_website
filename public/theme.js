(() => {
  const storageKey = "youzth-club-theme";
  const root = document.documentElement;
  const media = window.matchMedia("(prefers-color-scheme: dark)");

  const savedTheme = () => {
    try {
      const saved = window.localStorage.getItem(storageKey);
      if (saved === "light" || saved === "dark") return saved;
    } catch (error) {}
    return media.matches ? "dark" : "light";
  };

  const syncToggle = (theme) => {
    const isDark = theme === "dark";
    const label = isDark ? "Switch to light mode" : "Switch to dark mode";
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      button.setAttribute("aria-label", label);
      button.setAttribute("title", label);
      button.setAttribute("aria-pressed", String(isDark));
    });
  };

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
    syncToggle(theme);
  };

  if (!window.__youzthThemeControllerInitialized) {
    window.__youzthThemeControllerInitialized = true;
    document.addEventListener("click", (event) => {
      const button = event.target instanceof Element
        ? event.target.closest("[data-theme-toggle]")
        : null;
      if (!button) return;

      const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
      try {
        window.localStorage.setItem(storageKey, nextTheme);
      } catch (error) {}
      applyTheme(nextTheme);
    });

    media.addEventListener("change", (event) => {
      let saved = null;
      try {
        saved = window.localStorage.getItem(storageKey);
      } catch (error) {}
      if (!saved) applyTheme(event.matches ? "dark" : "light");
    });

    const observer = new MutationObserver(() => {
      if (document.querySelector("[data-theme-toggle]")) {
        syncToggle(root.dataset.theme);
        observer.disconnect();
      }
    });
    observer.observe(root, { childList: true, subtree: true });
  }

  applyTheme(savedTheme());

})();
