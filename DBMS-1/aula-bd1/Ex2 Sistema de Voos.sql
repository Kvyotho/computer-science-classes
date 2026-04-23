
CREATE TABLE IF NOT EXISTS Passageiros (
Cod_Passageiro VARCHAR(15) PRIMARY KEY,
Nome VARCHAR(20),
Sobrenome VARCHAR(50),
Data_nasc DATE,
Nacionalidade VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS Passageiros_Reservas (
Passageiros_Cod_Passageiro VARCHAR(15),
Reservas_de_Voo_Cod_Reserva INT,
PRIMARY KEY (Passageiros_Cod_Passageiro, Reservas_de_Voo_Cod_Reserva)
CONSTRAINT  
CONSTRAINT

CREATE TABLE IF NOT EXISTS Reservas_de_Voo (
Cod_Reserva INT PRIMARY KEY,
Data_reserva VARCHAR(45),
Forma_Pagamento ENUM(--------),
Valor_Total(10,2)

CREATE TABLE IF NOT EXISTS Aeronave (
Cod_Aeronave INT PRIMARY KEY,
Modelo VARCHAR(45),
Fabricante VARCHAR(45),
Ano YEAR(4),
Quantidade_Assentos INT,
Cias_Aereas_ID_CIA INT,
);

CREATE TABLE IF NOT EXISTS Cias_Aereas (
ID_Cia INT PRIMARY KEY,
Nome VARCHAR(45),
CNPJ VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS Voos (
ID_Voo INT PRIMARY KEY,
Assento VARCHAR(45) PRIMARY KEY,
Data_Partida DATE,
Data_Chegada_Prev DATE,
Hora_Partida TIME,
Hora_Chegada_Prev TIME,
Aeronave_Cod_Aeronave INT,
Aeroportos_Cod_Aeroporto_Partida VARCHAR(4),
Aeroportos_Cod_Aeroporto_Chegada VARCHAR(4),
Cias_Aereas_ID_CIA INT,
PRIMARY KEY (Aeronave_Cod_Aeronave, Aeroportos_Cod_Aeroporto_Partida, Aeroportos_Cod_Aeroporto_Chegada, Cias_Aereas_ID_CIA),
CONSTRAINT Aeronave_Cod_Aeronave FOREIGN KEY (Aeronave_Cod_Aeronave) REFERENCES Aeronave(Cod_Aeronave),
CONSTRAINT Aeroportos_Cod_Aeroporto_Partida FOREIGN KEY (Aeroportos_Cod_Aeroporto_Partida) REFERENCES Aeroportos(Cod_Aeroporto_Partida),
CONSTRAINT Aeroportos_Cod_Aeroporto_Chegada FOREIGN KEY (Aeroportos_Cod_Aeroporto_Chegada) REFERENCES Aeroportos(Cod_Aeroporto_Chegada),
CONSTRAINT Cias_Aereas_ID_CIA FOREIGN KEY (Cias_Aereas_ID_CIA) REFERENCES Cias_Aereas(ID_CIA)
);

CREATE TABLE IF NOT EXISTS Aeroportos (
Cod_Aeroporto VARCHAR(45) PRIMARY KEY,
----------
----------
---------
---------
----------
----------
);

CREATE TABLE IF NOT EXISTS Voo_Reservas (
Voos_ID_Voo INT,
Voos_Aeronave_Cod_Aeronave INT,
Voos_Aeroportos_Cod_Aeroporto_Partida VARCHAR(4),
Voos_Aeroportos_Cod_Aeroporto_Chegada VARCHAR(4),
Voos_Cias_Aereas_ID_CIA INT,
Voos_Assento VARCHAR(45),
Reservas_de_Voo_Cod_Reserva INT,
PRIMARY KEY (Voos_ID_Voo, Voos_Aeronave_Cod_Aeronave, Voos_Aeroportos_Cod_Aeroporto_Partida, Voos_Aeroportos_Cod_Aeroporto_Chegada, Voos_Cias_Aereas_ID_CIA, Voos_Assento, Reservas_de_Voo_Cod_Reserva),
CONSTRAINT Voos_ID_Voo FOREIGN KEY (Voos_ID_Voo) REFERENCES Voos(ID_Voo),
CONSTRAINT Voos_Aeronave_Cod_Aeronave FOREIGN KEY (Voos_Aeronave_Cod_Aeronave) REFERENCES Voos(Aeronave_Cod_Aeronave),
CONSTRAINT Voos_Aeroportos_Cod_Aeroporto_Partida FOREIGN KEY (Voos_Aeroportos_Cod_Aeroporto_Partida) REFERENCES Voos(Aeroportos_Cod_Aeroporto_Partida),
CONSTRAINT Voos_Aeroporto_Cod_Aeroporto_Chegada FOREIGN KEY (Voos_Aeroportos_Cod_Aeropoto_Chegada) REFERENCES Voos(Aeroportos_Cod_Aeroporto_Chegada),
CONSTRAINT Voos_Cias_Aereas_ID_CIA FOREIGN KEY (Voos_Cias_Aereas_ID_CIA) REFERENCES Voos(Cias_Aereas_ID_CIA),
CONSTRAINT Voos_Assento FOREIGN KEY (Voos_Assento) REFERENCES Voos(Assento),
CONSTRAINT Reservas_de_Voo_Cod_Reserva FOREIGN KEY (Reservas_de_Voo_Cod_Reserva) REFERENCES Reservas_De_Voo(Cod_Reserva)

