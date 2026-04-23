CREATE TABLE IF NOT EXISTS Pacientes (
CPF_Paciente VARCHAR(15) PRIMARY KEY,
Nome VARCHAR(45),
Data_nasc DATE,
Telefone VARCHAR(45),
Email VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS Consultas (
idConsultas INT PRIMARY KEY,
Anamnese TEXT,
Dia Date,
Hora TIME,
Pacientes_CPF_Paciente VARCHAR(15),
Medicos_CRM INT,
Medicos_UF CHAR(2),
Medicos_Departamentos_Cod_Especialidade INT,
PRIMARY KEY (Pacientes_CPF_Paciente, Medicos_CRM, Medicos_UF, Medicos_Departamentos_Cod_Especialidade),
CONSTRAINT Pacientes_CPF_Paciente FOREIGN KEY (Pacientes_CPF_Paciente) REFERENCES Pacientes(CPF_Paciente),
CONSTRAINT Medicos_CRM FOREIGN KEY (Medicos_CRM) REFERENCES Medicos(CRM),
CONSTRAINT Medicos_UF FOREIGN KEY (Medicos_UF) REFERENCES Medicos(UF),
CONSTRAINT Medicos_Departamentos_Cod_Especilidade FOREIGN KEY (Medicos_Departamentos_Cod_Especialidade) REFERENCES Medicos(Departamento_Cod_Especialidade)
);

CREATE TABLE IF NOT EXISTS Medicos (
CRM INT PRIMARY KEY,
UF CHAR(2) PRIMARY KEY,
Nome VARCHAR(45),
Email VARCHAR(45),
Telefone VARCHAR(45),
Departamentos_Cod_Especialidade INT,
PRIMARY KEY (Departamentos_Cod_Especialidade),
CONSTRAINT Departamentos_Cod_Especialidade FOREIGN KEY (Departamentos_Cod_Especialidade) REFERENCES Departamentos(Cod_Especialidade)
);

CREATE TABLE IF NOT EXISTS Departamentos (
Cod_Especialidade INT PRIMARY KEY,
Nome_Especialidade VARCHAR(45)
);

