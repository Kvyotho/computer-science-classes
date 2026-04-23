DROP DATABASE Cinema; 
CREATE DATABASE IF NOT EXISTS Cinema;
USE Cinema;

CREATE TABLE IF NOT EXISTS Sala (
ID_Sala INT PRIMARY KEY,
Nome VARCHAR(45),
Capacidade INT
);

CREATE TABLE IF NOT EXISTS Filmes (
ID_Filmes INT PRIMARY KEY,
Nome VARCHAR(45),
Distribuidora VARCHAR(45),
Tempo INT,
Diretor VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS Espectadores (
Cod_Espectador INT PRIMARY KEY,
Telefone VARCHAR(20),
Email VARCHAR(30),
Nome VARCHAR(100),
Data_Nasc Date
);

CREATE TABLE IF NOT EXISTS Ingressos (
ID_Ingressos INT PRIMARY KEY,
Date_Ing DATE,
Hora_Ing TIME,
Espectador INT,
CONSTRAINT Ingresso_Espectador FOREIGN KEY (Espectador) REFERENCES Espectadores(Cod_Espectador)
);

CREATE TABLE IF NOT EXISTS Sessoes (
ID_Sessao INT PRIMARY KEY,
Filmes INT,
Sala INT,
Ingressos INT,
Ingressos_Espec INT,
CONSTRAINT Sessoes_Filme FOREIGN KEY (Filmes) REFERENCES Filmes(ID_Filmes),
CONSTRAINT Sessoes_Sala FOREIGN KEY (Sala) REFERENCES Sala(ID_Sala),
CONSTRAINT Sessoes_Ingresso FOREIGN KEY (Ingressos) REFERENCES Ingressos(ID_Ingressos),
CONSTRAINT Sessoes_Ingresso_Espec FOREIGN KEY (Ingressos_Espec) REFERENCES Espectadores(Cod_Espectador)
);

