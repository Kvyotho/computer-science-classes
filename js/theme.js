
function applyTheme(theme) {
  if(theme === "light") {
    document.body.classList.add("light-mode");
  } else {
    document.body.classList.remove("light-mode");
  }
}

// Carrega settings do localStorage
const settings = JSON.parse(localStorage.getItem("settings")) || { theme: "dark" };
applyTheme(settings.theme);

// Para páginas com seletor de tema (como settings.html)
const themeSelect = document.getElementById("theme-select");
if(themeSelect) {
  themeSelect.value = settings.theme;
  themeSelect.addEventListener("change", () => {
    settings.theme = themeSelect.value;
    localStorage.setItem("settings", JSON.stringify(settings));
    applyTheme(settings.theme);
  });
}