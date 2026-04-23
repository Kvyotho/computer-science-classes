    document.getElementById("Formulario").addEventListener("submit", function(event) {
        event.preventDefault();

    //Adquirin informações do formulario
    const nome = document.getElementById("nome").value;
    const matricula = document.getElementById("matricula").value;
    const nota1 = parseFloat(document.getElementById("nota1").value);
    const nota2 = parseFloat(document.getElementById("nota2").value);

    //Calcular a média
    const media = (nota1 + nota2) / 2;

    //Determinar a situação do aluno
    let situacao
            if (media >=6) {
        situacao = "Aprovado";
            } else {
        situacao = "Reprovado"
    }

            //Anexar informações para a tabela
    const table = document.getElementById("Tabela").getElementsByTagName("tbody")[0];
    const newRow = table.insertRow();
    const cells = [
    newRow.insertCell(),
    newRow.insertCell(),
    newRow.insertCell(),
    newRow.insertCell(),
    newRow.insertCell(),
    newRow.insertCell()
    ];

    cells[0].textContent = nome;
    cells[1].textContent = matricula;
    cells[2].textContent = nota1;
    cells[3].textContent = nota2;
    cells[4].textContent = media.toFixed(2);
    cells[5].textContent = situacao;
        });