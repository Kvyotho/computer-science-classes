CREATE DATABASE IF NOT EXISTS projeto2_cc3mb;
USE projeto2_cc3mb;

CREATE TABLE IF NOT EXISTS atendentes (
    matricula CHAR(3) PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    matricula_responsavel CHAR(3),  #atendente senior
    FOREIGN KEY (matricula_responsavel) REFERENCES atendentes(matricula)
);

CREATE TABLE IF NOT EXISTS mesas (
    codigo_mesa CHAR(2) PRIMARY KEY,  #limita os codigos/ids da mesa a 2 digitos
    qtd_cadeiras INT NOT NULL
);

CREATE TABLE IF NOT EXISTS clientes (
    codigo_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    cpf CHAR(11) UNIQUE,
    endereco VARCHAR(100),
    mesa_atual CHAR(2),  #fk referenciando a tabela de mesas
    FOREIGN KEY (mesa_atual) REFERENCES mesas(codigo_mesa)
);

CREATE TABLE IF NOT EXISTS pratos (  #tabela para os pratos disponiveis com desc e preço
    codigo_prato INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    descricao VARCHAR(255),
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS bebidas (  #tabela para bebidas disponiveis com desc e preço
    codigo_bebida INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    descricao VARCHAR(255),
    preco DECIMAL(10,2) NOT NULL CHECK (preco > 0)
);

CREATE TABLE IF NOT EXISTS pedidos (  
    codigo_pedido INT AUTO_INCREMENT PRIMARY KEY,
    codigo_cliente INT NOT NULL,
    matricula_atendente CHAR(3) NOT NULL,
    codigo_mesa CHAR(2) NOT NULL,
    data_hora_inicio DATETIME NOT NULL,  #permite determinar a duração do pedido ao ser utilizado numa função (inicio - fim)
    data_hora_fim DATETIME,
    FOREIGN KEY (codigo_cliente) REFERENCES clientes(codigo_cliente),
    FOREIGN KEY (matricula_atendente) REFERENCES atendentes(matricula),
    FOREIGN KEY (codigo_mesa) REFERENCES mesas(codigo_mesa)
);

CREATE TABLE IF NOT EXISTS pedido_pratos (  #tabela para os pratos nos pedidos
    codigo_pedido INT,
    codigo_prato INT,
    quantidade INT NOT NULL DEFAULT 1,
    PRIMARY KEY (codigo_pedido, codigo_prato),
    FOREIGN KEY (codigo_pedido) REFERENCES pedidos(codigo_pedido),
    FOREIGN KEY (codigo_prato) REFERENCES pratos(codigo_prato)
);

CREATE TABLE IF NOT EXISTS pedido_bebidas (  #tabela para as bebidas nos pedidos
    codigo_pedido INT,
    codigo_bebida INT,
    quantidade INT NOT NULL DEFAULT 1,
    PRIMARY KEY (codigo_pedido, codigo_bebida),
    FOREIGN KEY (codigo_pedido) REFERENCES pedidos(codigo_pedido),
    FOREIGN KEY (codigo_bebida) REFERENCES bebidas(codigo_bebida)
);

CREATE TABLE IF NOT EXISTS atendente_telefones (  #tabela para contato de telefone dos atendentes
    id_telefone INT AUTO_INCREMENT PRIMARY KEY,
    matricula_atendente CHAR(3) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    FOREIGN KEY (matricula_atendente) REFERENCES atendentes(matricula)
);