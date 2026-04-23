function desenharCartela() {

    //Seleciona onde criar o elemento
    const pai_div_cartela = document.getElementById('body_cartelas');

    //Cria uma div para cartela
    const div_cartela = document.createElement('div');
    div_cartela.className = 'cartela';

    //Insere div dentro do pai
    pai_div_cartela.appendChild(div_cartela);

    //Cria um elemento de de texto para o nome do jogador
    const h4_jogador = document.createElement('h4');
    h4_jogador.innerText = "Nome Jogador";

    //Insere o nome do jogador
    div_cartela.appendChild(h4_jogador);

    //Criar tabela do bingo
    const tabela = document.createElement('table');
    const thead = document.createElement('thead');
    const tbody = document.createElement('tbody');

    
    //Criar elementos do thead
    const thB = document.createElement('th');
    const thI = document.createElement('th');
    const thN = document.createElement('th');
    const thG = document.createElement('th');
    const thO = document.createElement('th');
    
    thB.innerText = 'B'
    thI.innerText = 'I'
    thN.innerText = 'N'
    thG.innerText = 'G'
    thO.innerText = 'O'
    
    //Insere os ths no thead
    thead.appendChild(thB)
    thead.appendChild(thI)
    thead.appendChild(thN)
    thead.appendChild(thG)
    thead.appendChild(thO)
    
    
    //fix
    for(var i = 0; i < 5; i++)(
        const tr = document.createElement('tr');
        for(var j = 0; j < 5; j++)(
            const td = document.createElement('td');
            td.innerText = 'X';
            tr.appendChild(td);
        )
        )

    //Inserir na tabela
    tabela.appendChild(thead);
    tabela.appendChild(tbody);

    div_cartela.appendChild(tabela);

 
    




}