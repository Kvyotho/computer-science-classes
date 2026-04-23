

(function () {
  // ===== Exemplo de tarefas (somente usado se localStorage vazio) =====
  const exampleTasks = [
// Tarefas atrasadas
    { titulo: "Lista 1 - Limites e Derivadas", materia: "Cálculo", prioridade: "alta", status: "atrasada", data: "2025-11-05" },
    { titulo: "Entregar relatório - Algoritmos", materia: "Algoritmos", prioridade: "média", status: "atrasada", data: "2025-11-06" },
    { titulo: "Revisar Estruturas de Dados", materia: "Estruturas de Dados", prioridade: "baixa", status: "atrasada", data: "2025-11-08" },

    // Tarefas do dia atual
    { titulo: "Exercícios de Programação Orientada a Objetos", materia: "Java", prioridade: "alta", status: "pendente", data: "2025-11-12" },
    { titulo: "Ler capítulo de Sistemas Operacionais", materia: "SO", prioridade: "média", status: "pendente", data: "2025-11-12" },

    // Tarefas futuras
    { titulo: "Preparar apresentação - Banco de Dados", materia: "BD", prioridade: "alta", status: "pendente", data: "2025-11-14" },
    { titulo: "Estudar programação Python", materia: "Python", prioridade: "média", status: "pendente", data: "2025-11-15" },
    { titulo: "Fazer exercícios de Redes", materia: "Redes", prioridade: "baixa", status: "pendente", data: "2025-11-16" },

    // Mais tarefas atrasadas
    { titulo: "Enviar relatório de Inteligência Artificial", materia: "IA", prioridade: "alta", status: "atrasada", data: "2025-11-01" },
    { titulo: "Revisar conceitos de Computação Gráfica", materia: "CG", prioridade: "média", status: "atrasada", data: "2025-11-03" },

    // Tarefas futuras
    { titulo: "Estudar Engenharia de Software", materia: "Eng. de Software", prioridade: "baixa", status: "pendente", data: "2025-11-18" },
    { titulo: "Praticar exercícios de Inteligência Artificial", materia: "IA", prioridade: "alta", status: "pendente", data: "2025-11-20" },
    { titulo: "Fazer exercícios de Banco de Dados", materia: "BD", prioridade: "média", status: "pendente", data: "2025-11-22" },
    { titulo: "Revisar Sistemas Distribuídos", materia: "SO", prioridade: "baixa", status: "pendente", data: "2025-11-25" },

    // Tarefas do final do mês
    { titulo: "Preparar resumo de Cálculo", materia: "Cálculo", prioridade: "alta", status: "pendente", data: "2025-11-28" },
    { titulo: "Estudar Inteligência Computacional", materia: "IA", prioridade: "média", status: "pendente", data: "2025-11-29" },
    { titulo: "Fazer exercícios de Estruturas de Dados", materia: "Estruturas de Dados", prioridade: "baixa", status: "pendente", data: "2025-11-30" },
];

  // ===== Util: adiciona listener somente se elemento existir =====
  function safeAddEvent(idOrEl, event, handler) {
    const el = (typeof idOrEl === "string") ? document.getElementById(idOrEl) : idOrEl;
    if (el) el.addEventListener(event, handler);
  }

  // ===== Inicializa localStorage com exemplos se estiver vazio =====
  if (!localStorage.getItem("tasks") || JSON.parse(localStorage.getItem("tasks")).length === 0) {
    localStorage.setItem("tasks", JSON.stringify(exampleTasks));
    console.log("✅ Tarefas de exemplo carregadas.");
  } else {
    console.log("ℹ️ Tarefas já existentes no localStorage. Nenhuma modificação feita.");
  }

  // ===== Dados =====
  let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
  let editIndex = null; // índice da tarefa sendo editada, null se for nova

  // ===== Elementos (guardados em variáveis para não chamar getElement toda hora) =====
  const container = document.getElementById("tasks-container");
  const searchInput = document.getElementById("search-input");
  const filterStatus = document.getElementById("filter-status");
  const filterPriority = document.getElementById("filter-priority");

  const counts = {
    pendente: document.getElementById("count-pending"),
    concluida: document.getElementById("count-completed"),
    atrasada: document.getElementById("count-late"),
  };

  const modal = document.getElementById("task-modal");
  const addTaskBtn = document.getElementById("add-task-btn");
  const saveTaskBtn = document.getElementById("save-task");
  const cancelTaskBtn = document.getElementById("cancel-task");

  // ===== Helpers =====
  function saveToStorage() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }

  function clearModalFields() {
    const t = document.getElementById("new-title");
    const s = document.getElementById("new-subject");
    const p = document.getElementById("new-priority");
    const d = document.getElementById("new-date");
    if (t) t.value = "";
    if (s) s.value = "";
    if (p) p.value = "baixa";
    if (d) d.value = "";
    editIndex = null;
  }

  function openModalForNew() {
    clearModalFields();
    if (modal) modal.classList.remove("hidden");
  }

  function openModalForEdit(index) {
    const t = tasks[index];
    if (!t) return;
    document.getElementById("new-title").value = t.titulo || "";
    document.getElementById("new-subject").value = t.materia || "";
    document.getElementById("new-priority").value = t.prioridade || "baixa";
    document.getElementById("new-date").value = t.data || "";
    editIndex = index;
    if (modal) modal.classList.remove("hidden");
  }

  function closeModal() {
    if (modal) modal.classList.add("hidden");
    clearModalFields();
  }

  // ===== Atualiza statuses com base na data (atrasada) =====
  function updateStatuses() {
    const today = new Date().toISOString().split("T")[0];
    tasks.forEach(t => {
      if (t.status !== "concluida" && t.data && t.data < today) {
        t.status = "atrasada";
      } else if (t.status === "atrasada" && t.data && t.data >= today) {
        t.status = "pendente";
      }
    });
    saveToStorage();
  }

  // ===== Renderização =====
  function renderTasks(list = tasks) {
    if (!container) return;
    container.innerHTML = "";

    if (!list || list.length === 0) {
      container.innerHTML = "<p>Nenhuma tarefa encontrada.</p>";
      return;
    }

    list.forEach((task, index) => {
      const div = document.createElement("div");
      div.className = "task-card";

      // meta / status colors
      const statusLabel = task.status || "pendente";
      const statusColor = statusLabel === "concluida" ? "#4caf50" : (statusLabel === "atrasada" ? "#f44336" : "#ffc107");

      div.innerHTML = `
        <div>
          <h4>${escapeHtml(task.titulo || "—")}</h4>
          <p class="task-meta">${escapeHtml(task.materia || "")} • ${formatDate(task.data)} • <span style="color:${statusColor}; font-weight:600;">${statusLabel}</span></p>
        </div>
        <div class="task-actions" data-index="${index}">
          <button class="btn-done" title="Marcar como concluída">✔</button>
          <button class="btn-edit" title="Editar">✎</button>
          <button class="btn-delete" title="Excluir">🗑</button>
        </div>
      `;

      container.appendChild(div);

      // eventos dos botões (delegação simples)
      const actions = div.querySelector(".task-actions");
      if (actions) {
        const i = index;
        const btnDone = actions.querySelector(".btn-done");
        const btnEdit = actions.querySelector(".btn-edit");
        const btnDelete = actions.querySelector(".btn-delete");

        if (btnDone) btnDone.addEventListener("click", () => { markDone(i); });
        if (btnEdit) btnEdit.addEventListener("click", () => { openModalForEdit(i); });
        if (btnDelete) btnDelete.addEventListener("click", () => {
          if (confirm(`Excluir tarefa "${tasks[i].titulo}"?`)) deleteTask(i);
        });
      }
    });

    updateCounts();
    saveToStorage();
  }

  // ===== Escapar texto simples para evitar undefined/xss na UI =====
  function escapeHtml(str) {
    if (typeof str !== "string") return str ?? "";
    return str.replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]);
  }

  function formatDate(s) {
    if (!s) return "";
    // espera YYYY-MM-DD
    try {
      const d = new Date(s);
      if (isNaN(d)) return s;
      return d.toLocaleDateString("pt-BR");
    } catch {
      return s;
    }
  }

  // ===== Ações =====
  function markDone(index) {
    if (!tasks[index]) return;
    tasks[index].status = "concluida";
    saveToStorage();
    applyFilters(); // re-render com filtros
  }

  function deleteTask(index) {
    if (index < 0 || index >= tasks.length) return;
    tasks.splice(index, 1);
    saveToStorage();
    applyFilters();
  }

  function editSaveFromModal() {
    const title = document.getElementById("new-title").value.trim();
    const subject = document.getElementById("new-subject").value.trim();
    const priority = document.getElementById("new-priority").value;
    const date = document.getElementById("new-date").value;

    if (!title || !subject || !date) {
      alert("Preencha todos os campos (Título, Matéria, Data).");
      return;
    }

    if (editIndex === null) {
      // criar nova
      tasks.push({ titulo: title, materia: subject, prioridade: priority, status: "pendente", data: date });
    } else {
      // editar existente
      const t = tasks[editIndex];
      t.titulo = title;
      t.materia = subject;
      t.prioridade = priority;
      t.data = date;
      // não altera status automaticamente ao editar
    }

    saveToStorage();
    closeModal();
    applyFilters();
  }

  // ===== Filtros =====
  function applyFilters() {
    const text = (searchInput && searchInput.value) ? searchInput.value.toLowerCase() : "";
    const status = filterStatus ? filterStatus.value : "";
    const priority = filterPriority ? filterPriority.value : "";

    const filtered = tasks.filter(t => {
      const matchText = (t.titulo || "").toLowerCase().includes(text) || (t.materia || "").toLowerCase().includes(text);
      const matchStatus = status ? (t.status === status) : true;
      const matchPriority = priority ? (t.prioridade === priority) : true;
      return matchText && matchStatus && matchPriority;
    });

    renderTasks(filtered);
  }

  // ===== Contadores =====
  function updateCounts() {
    if (!counts.pendente || !counts.concluida || !counts.atrasada) return;
    counts.pendente.textContent = tasks.filter(t => t.status === "pendente").length;
    counts.concluida.textContent = tasks.filter(t => t.status === "concluida").length;
    counts.atrasada.textContent = tasks.filter(t => t.status === "atrasada").length;
  }

  // ===== Listeners seguros =====
  safeAddEvent("toggle-btn", "click", () => {
    const sb = document.getElementById("sidebar");
    if (sb) sb.classList.toggle("close");
  });

  safeAddEvent(addTaskBtn, "click", openModalForNew);
  safeAddEvent(cancelTaskBtn, "click", closeModal);
  safeAddEvent(saveTaskBtn, "click", editSaveFromModal);

  // filtros inputs
  if (searchInput) searchInput.addEventListener("input", applyFilters);
  if (filterStatus) filterStatus.addEventListener("change", applyFilters);
  if (filterPriority) filterPriority.addEventListener("change", applyFilters);

  // Sidebar quick filters (se existirem no DOM)
  safeAddEvent("view-all", "click", () => renderTasks(tasks));
  safeAddEvent("view-pending", "click", () => renderTasks(tasks.filter(t => t.status === "pendente")));
  safeAddEvent("view-completed", "click", () => renderTasks(tasks.filter(t => t.status === "concluida")));
  safeAddEvent("view-late", "click", () => renderTasks(tasks.filter(t => t.status === "atrasada")));

  // ===== Inicialização =====
  updateStatuses();
  updateCounts();
  renderTasks(tasks);

  // ===== Expor algumas funções para console debugging (opcional) =====
  window.__sgt = {
    tasks,
    saveToStorage,
    renderTasks,
    updateCounts,
    updateStatuses
  };
})();
