const monthYear = document.getElementById("month-year");
const grid = document.getElementById("calendar-grid");
const btnPrev = document.getElementById("prev-month");
const btnNext = document.getElementById("next-month");

let currentDate = new Date();

// carrega tarefas do localStorage
const tasks = JSON.parse(localStorage.getItem("tasks")) || [];

function renderCalendar(date) {
  grid.innerHTML = "";

  const year = date.getFullYear();
  const month = date.getMonth();

  const firstDay = new Date(year, month, 1);
  const lastDay = new Date(year, month + 1, 0);

  const startDay = firstDay.getDay();
  const daysInMonth = lastDay.getDate();

  monthYear.textContent = date.toLocaleDateString("pt-BR", {
    month: "long",
    year: "numeric"
  });

  // dias do mês anterior
  const prevLastDay = new Date(year, month, 0).getDate();
  for (let i = startDay - 1; i >= 0; i--) {
    const div = document.createElement("div");
    div.className = "day other-month";
    div.textContent = prevLastDay - i;
    grid.appendChild(div);
  }

  // dias do mês atual
  for (let day = 1; day <= daysInMonth; day++) {
    const div = document.createElement("div");
    div.className = "day";
    div.textContent = day;

    const dateStr = `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;

    // verifica se tem tarefa neste dia
    const hasTask = tasks.some(t => t.data === dateStr);
    if (hasTask) div.classList.add("has-task");

div.addEventListener("click", () => {
  const dayTasks = tasks.filter(t => t.data === dateStr);
  const modal = document.getElementById("task-modal");
  const modalDate = document.getElementById("modal-date");
  const modalList = document.getElementById("modal-task-list");

  modalDate.textContent = dayTasks.length
    ? `📅 ${dayTasks.length} tarefa(s) em ${dateStr}`
    : `Nenhuma tarefa em ${dateStr}`;

  modalList.innerHTML = "";

  if (dayTasks.length) {
    dayTasks.forEach(t => {
      const li = document.createElement("li");
      li.innerHTML = `
        <strong>${t.titulo}</strong>
        <span>${t.materia}</span>
        <small>Prioridade: ${t.prioridade}</small>
      `;
      modalList.appendChild(li);
    });
  }

  modal.style.display = "flex";
});

    grid.appendChild(div);
  }

  // dias do próximo mês para completar a grade (6 linhas)
  const totalCells = grid.children.length;
  const nextDays = 42 - totalCells;
  for (let i = 1; i <= nextDays; i++) {
    const div = document.createElement("div");
    div.className = "day other-month";
    div.textContent = i;
    grid.appendChild(div);
  }
}

btnPrev.addEventListener("click", () => {
  currentDate.setMonth(currentDate.getMonth() - 1);
  renderCalendar(currentDate);
});

btnNext.addEventListener("click", () => {
  currentDate.setMonth(currentDate.getMonth() + 1);
  renderCalendar(currentDate);
});

renderCalendar(currentDate);

// Fechar modal
document.getElementById("close-modal").addEventListener("click", () => {
  document.getElementById("task-modal").style.display = "none";
});

window.addEventListener("click", (e) => {
  const modal = document.getElementById("task-modal");
  if (e.target === modal) modal.style.display = "none";
});