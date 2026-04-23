const themeSelect = document.getElementById("theme-select");

// Função para aplicar o tema
function applyTheme(theme) {
  if(theme === "light") {
    document.body.classList.add("light-mode");
  } else {
    document.body.classList.remove("light-mode");
  }
}

// Carregar preferências do localStorage
const settings = JSON.parse(localStorage.getItem("settings")) || {
  theme: "dark",
  notifications: true,
  calendarView: "month"
};

// Aplicar tema ao carregar
applyTheme(settings.theme);

// Ajustar controles
themeSelect.value = settings.theme;

// Salvar configurações
document.getElementById("save-settings").addEventListener("click", () => {
  const newSettings = {
    theme: themeSelect.value,
    notifications: document.getElementById("notif-toggle").checked,
    calendarView: document.getElementById("calendar-view").value
  };
  localStorage.setItem("settings", JSON.stringify(newSettings));

  // Aplica o tema imediatamente
  applyTheme(newSettings.theme);

  showNotification("Configurações salvas com sucesso!");
});


function showNotification(message, duration = 3000) {
    const container = document.getElementById("notification-container");
    const notif = document.createElement("div");
    notif.className = "notification";
    notif.textContent = message;
    container.appendChild(notif);

    // força o trigger da animação
    requestAnimationFrame(() => {
        notif.classList.add("show");
    });

    // remover após o tempo
    setTimeout(() => {
        notif.classList.remove("show");
        setTimeout(() => container.removeChild(notif), 400); // espera a transição
    }, duration);
}
