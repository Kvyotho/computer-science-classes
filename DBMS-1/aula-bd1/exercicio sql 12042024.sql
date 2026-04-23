CREATE TABLE IF NOT EXISTS Atestado (
id_atestado INT(11) PRIMARY KEY,
resultado_riscos VARCHAR(100) NOT NULL,
resultado VARCHAR(100) NOT NULL,
observacoes VARCHAR(300) NOT NULL,
medico_id INT(11) NOT NULL,
CONSTRAINT medico_id FOREIGN KEY (medico_id) REFERENCES Medico(id_medico)
);

CREATE TABLE IF NOT EXISTS Cargo (
id_cargo INT(11) PRIMARY KEY,
nome VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS Riscos_Ocupacionais (
id_riscos INT(11) PRIMARY KEY,
nome VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS Cargo_Riscos (
id_cargo INT(11),
id_riscos INT(11),
PRIMARY KEY (id_cargo, id_riscos),
CONSTRAINT id_cargo FOREIGN KEY (id_cargo) REFERENCES Cargo(id_cargo),
CONSTRAINT id_riscos FOREIGN KEY (id_riscos) REFERENCES Riscos_Ocupacionais(id_riscos)
);

CREATE TABLE IF NOT EXISTS Empresa (
id_empresa INT(11) PRIMARY KEY,
cnpj VARCHAR(20) NOT NULL,
nome_fantasia VARCHAR(50) NOT NULL,
endereço VARCHAR(200) NOT NULL,
telefone VARCHAR(20) NOT NULL,
FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa)
);

CREATE TABLE IF NOT EXISTS Exame (
id_exame INT(11) PRIMARY KEY,
especialidade VARCHAR(50) NOT NULL,
data_realizacao DATE NOT NULL,
tipo_exame INT(11),
resultado_exame INT(11),
CONSTRAINT tipo_exame FOREIGN KEY (tipo_exame) REFERENCES Tipo_Exame(id_tipo_exame),
CONSTRAINT resultado_exame FOREIGN KEY (resultado_exame) REFERENCES Resultado_Exame(id_tipo_resultado_exame)
);

CREATE TABLE IF NOT EXISTS Tipo_Exame (
id_tipo_exame INT(11) PRIMARY KEY,
tipo VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Resultado_Exame (
id_tipo_resultado_exame INT(11),
tipo VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS Funcionario (
id_funcionario INT(11) PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
cpf VARCHAR(20) NOT NULL,
data_nascimento DATE NOT NULL,
endereco VARCHAR(200) NOT NULL,
telefone VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Medico (
id_medico INT(11) PRIMARY KEY,
cm INT(11) NOT NULL,
nome VARCHAR(100) NOT NULL,
cpf VARCHAR(20) NOT NULL,
especialidade VARCHAR(50) NOT NULL,
data_nascimento DATE NOT NULL,
endereco VARCHAR(200) NOT NULL,
telefone VARCHAR(20)
);




