CREATE DATABASE Rede_Social;
USE Rede_Social;

CREATE TABLE IF NOT EXISTS Usuarios (
ID_Usuario INT PRIMARY KEY,
Nome VARCHAR(45),
Sobrenome VARCHAR(45),
Email VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS Comentarios (
ID_Comentario INT PRIMARY KEY,
Texto_Coment Text,
Datahora DATETIME,
Usuarios INT PRIMARY KEY,
Postagens INT PRIMARY KEY,
CONSTRAINT Usuarios FOREIGN KEY (Usuarios) REFERENCES ID_Usuario(Usuarios),
CONSTRAINT Postagens FOREIGN KEY (Postagens) REFERENCES ID_Post(Postagens)
);

CREATE TABLE IF NOT EXISTS Grupos (
ID_Grupo INT PRIMARY KEY,
Nome_Grupo VARCHAR(45),
Descricao TEXT
);

CREATE TABLE IF NOT EXISTS Postagens (
ID_Post INT PRIMARY KEY,
Texto_Post Text,
Imagem_Post BLOB,
Data_Hora_Post DATETIME,
Usuarios INT PRIMARY KEY,
CONSTRAINT Usuarios_Post FOREIGN KEY (Usuarios) REFERENCES ID_Usuario(Usuarios)
);

CREATE TABLE IF NOT EXISTS Seguidores_Usuarios (
Seguidor INT PRIMARY KEY,
Seguido INT PRIMARY KEY,
CONSTRAINT Usuario_Seguidor FOREIGN KEY (Seguidor) REFERENCES ID_Usuario(Usuarios),
CONSTRAINT Usuario_Seguido FOREIGN KEY (Seguido) REFERENCES ID_Usuario(Usuarios)
);

CREATE TABLE IF NOT EXISTS Usuarios_Grupos (
Usuarios INT PRIMARY KEY,
Grupos INT PRIMARY KEY,
CONSTRAINT Usuarios FOREIGN KEY (Usuarios) REFERENCES ID_Usuario(Usuarios),
CONSTRAINT Grupos FOREIGN KEY (Grupos) REFERENCES ID_Grupo(Grupos)
);

