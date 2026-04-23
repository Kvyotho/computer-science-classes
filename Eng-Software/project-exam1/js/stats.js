// ======= LEITURA DAS TAREFAS =======
const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
const hoje = new Date();
hoje.setHours(0, 0, 0, 0); // compara apenas a data, ignora hora/minuto

// ======= AGRUPAMENTOS =======
const concluidas = tasks.filter(t => t.status === "concluida").length;

const atrasadas = tasks.filter(t => {
  const tarefaData = new Date(t.data);
  return tarefaData < hoje && t.status !== "concluida";
}).length;

const pendentes = tasks.filter(t => {
  const tarefaData = new Date(t.data);
  return tarefaData >= hoje && t.status !== "concluida";
}).length;

// ======= EXIBIÇÃO NUMÉRICA E TAXA =======
const total = tasks.length;
const taxaConclusao = total ? ((concluidas / total) * 100).toFixed(1) : 0;

document.getElementById("completion-rate").textContent = `${taxaConclusao}%`;
document.getElementById("completed-tasks").textContent = concluidas;
document.getElementById("pending-tasks").textContent = pendentes;
document.getElementById("late-tasks").textContent = atrasadas;

// ======= GRÁFICO DE PIZZA =======
const ctx = document.getElementById("tasks-chart").getContext("2d");
new Chart(ctx, {
  type: "pie",
  data: {
    labels: ["Concluídas", "Pendentes", "Atrasadas"],
    datasets: [{
      data: [concluidas, pendentes, atrasadas],
      backgroundColor: ["#4CAF50", "#FFC107", "#F44336"],
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "bottom",
        labels: { color: "#e3e3e3", font: { size: 14 } }
      }
    }
  }
});

// ======= MÉDIAS SEMANAIS =======
function calcularMediaSemanal() {
  const porSemana = {};

  tasks.forEach(t => {
    const data = new Date(t.data);
    const ano = data.getFullYear();
    const semana = Math.ceil(
      ((data - new Date(ano, 0, 1)) / 86400000 + new Date(ano, 0, 1).getDay() + 1) / 7
    );

    const chave = `${ano}-S${semana}`;
    porSemana[chave] ??= { total: 0, concluidas: 0 };
    porSemana[chave].total++;
    if (t.status === "concluida") porSemana[chave].concluidas++;
  });

  const medias = Object.entries(porSemana).map(([semana, dados]) => ({
    semana,
    media: ((dados.concluidas / dados.total) * 100).toFixed(1)
  }));

  return medias;
}

// ======= MOSTRAR MÉDIAS =======
const medias = calcularMediaSemanal();
const mediaContainer = document.getElementById("weekly-averages");

if (medias.length === 0) {
  mediaContainer.innerHTML = "<p>Sem tarefas registradas.</p>";
} else {
  mediaContainer.innerHTML = `
    <h3>Médias Semanais</h3>
    ${medias
      .map(m => `<p><strong>${m.semana}:</strong> ${m.media}% concluídas</p>`)
      .join("")}
  `;
}
