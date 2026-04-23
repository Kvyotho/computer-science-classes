DROP DATABASE Eventos;
CREATE DATABASE IF NOT EXISTS Eventos;
USE EVENTOS;

CREATE TABLE IF NOT EXISTS Locais (
ID_Local INT PRIMARY KEY,
Nome VARCHAR(45),
Logradouro VARCHAR(45),
Numero INT,
Bairro VARCHAR(45),
Cidade VARCHAR(45),
UF CHAR(2),
CEP VARCHAR(45),
Capacidade INT
);

CREATE TABLE IF NOT EXISTS Participantes (
Num_Insc INT,
CPF VARCHAR(45),
Nome VARCHAR(45),
Data_Nasc DATE,
Empresa VARCHAR(45),
PRIMARY KEY (Num_Insc, CPF)
);

CREATE TABLE IF NOT Exists Eventos (
ID_Evento INT PRIMARY KEY,
Nome VARCHAR(45),
Data_Evento DATE,
Entidade_Promotora VARCHAR(45),
Locais INT,
CONSTRAINT Evento_Local FOREIGN KEY (Locais) REFERENCES Locais(ID_Local)
);

CREATE TABLE IF NOT EXISTS Atividades (
ID_Atividade INT PRIMARY KEY,
Nome VARCHAR(45),
Data_Atividade DATE,
Hora_Atividade TIME,
Evento INT,
Local_Atividade INT,
CONSTRAINT Evento_Atividade FOREIGN KEY (Evento) REFERENCES Eventos(ID_Evento),
CONSTRAINT Local_Atividade FOREIGN KEY (Local_Atividade) REFERENCES Locais(ID_Local)
);

CREATE TABLE IF NOT EXISTS Participantes_Eventos (
Num_Inscricao INT PRIMARY KEY,
CPF VARCHAR(45),
Evento INT,
Local_Part_Evento INT,
CONSTRAINT Part_Event_Inscricao FOREIGN KEY (Num_Inscricao) REFERENCES Participantes(Num_Insc),
CONSTRAINT Part_Event_CPF FOREIGN KEY (CPF) REFERENCES Participantes(CPF),
CONSTRAINT Part_Event_Evento FOREIGN KEY (Evento) REFERENCES Eventos(ID_Evento),
CONSTRAINT Part_Event_Local FOREIGN KEY (Local_Part_Evento) REFERENCES Locais(ID_Local)
);

CREATE TABLE IF NOT EXISTS Participantes_Atividades (
Num_Insc INT,
CPF VARCHAR(45),
Atividade INT,
Evento INT,
Local_Part_Ativ INT,
CONSTRAINT Part_Ativ_Num_Insc FOREIGN KEY (Num_Insc) REFERENCES Participantes(Num_Insc),
CONSTRAINT Part_Ativ_CPF FOREIGN KEY (CPF) REFERENCES Participantes(CPF),
CONSTRAINT Part_Ativ_Atividade FOREIGN KEY (Atividade) REFERENCES Atividades(ID_Atividade),
CONSTRAINT Part_Ativ_Eventos FOREIGN KEY (Evento) REFERENCES Eventos(ID_Evento),
CONSTRAINT Part_Ativ_Local FOREIGN KEY (Local_Part_Ativ) REFERENCES Locais(Local_Atividade)
);
