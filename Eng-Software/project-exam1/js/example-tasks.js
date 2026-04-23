    // === Tarefas de exemplo para Ciência da Computação ===
    const exampleTasks = [
    {
        titulo: "Lista 1 - Limites e Derivadas",
        materia: "Cálculo",
        prioridade: "alta",
        status: "pendente",
        data: "2025-11-15"
    },
    {
        titulo: "Projeto - Modelo Relacional",
        materia: "Banco de Dados",
        prioridade: "media",
        status: "pendente",
        data: "2025-11-18"
    },
    {
        titulo: "Casos de Uso - Sistema de Biblioteca",
        materia: "Engenharia de Software",
        prioridade: "baixa",
        status: "pendente",
        data: "2025-11-10"
    },
    {
        titulo: "Resumo - Arquitetura RISC x CISC",
        materia: "Arquitetura de Computadores",
        prioridade: "media",
        status: "pendente",
        data: "2025-11-20"
    },
    {
        titulo: "Prática de SQL Avançado",
        materia: "Banco de Dados",
        prioridade: "alta",
        status: "pendente",
        data: "2025-11-22"
    }
    ];

  // === Inicializa localStorage apenas se estiver vazio ===
if (!localStorage.getItem("tasks") || JSON.parse(localStorage.getItem("tasks")).length === 0) {
  localStorage.setItem("tasks", JSON.stringify(exampleTasks));
  console.log("✅ Tarefas de exemplo carregadas.");
} else {
  console.log("ℹ️ Tarefas já existentes no localStorage. Nenhuma modificação feita.");
}

// ✅ Carrega as tarefas salvas
const tasks = JSON.parse(localStorage.getItem("tasks")) || [];

// Inicialização
updateCounts();
renderTasks(tasks);