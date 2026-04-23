CREATE DATABASE IF NOT EXISTS projeto1_cc3mb;
USE projeto1_cc3mb;


CREATE TABLE IF NOT EXISTS professores (
    matricula_professor VARCHAR(4) PRIMARY KEY,  #limita o matricula do professor a 4 digitos
    nome_professor VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL  #limita email do professor a ser único
);

CREATE TABLE IF NOT EXISTS cursos (
    codigo_curso INT PRIMARY KEY,
    nome_curso VARCHAR(100) NOT NULL,
    carga_horaria_total INT DEFAULT 3600,  #define a carga horaria padrao como 3600h
    matricula_coordenador VARCHAR(4),
    FOREIGN KEY (matricula_coordenador) REFERENCES professores(matricula_professor)
);

CREATE TABLE IF NOT EXISTS materias (
    codigo_materia INT PRIMARY KEY,
    nome_materia VARCHAR(60) NOT NULL,
    carga_horaria INT NOT NULL CHECK (carga_horaria >= 40)  #verifica se a carga horaria tem no minimo 40h
);

CREATE TABLE IF NOT EXISTS curso_materia (
    codigo_curso INT,
    codigo_materia INT,
    PRIMARY KEY (codigo_curso, codigo_materia),
    FOREIGN KEY (codigo_curso) REFERENCES cursos(codigo_curso),
    FOREIGN KEY (codigo_materia) REFERENCES materias(codigo_materia)
);

CREATE TABLE IF NOT EXISTS pre_requisitos (
    materia_codigo INT,
    pre_requisito_codigo INT,
    PRIMARY KEY (materia_codigo, pre_requisito_codigo),
    FOREIGN KEY (materia_codigo) REFERENCES materias(codigo_materia),
    FOREIGN KEY (pre_requisito_codigo) REFERENCES materias(codigo_materia)
);

CREATE TABLE IF NOT EXISTS alunos (
    matricula_aluno INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    codigo_curso INT,
    FOREIGN KEY (codigo_curso) REFERENCES cursos(codigo_curso)
);

CREATE TABLE IF NOT EXISTS aluno_emails (
    id_email INT PRIMARY KEY,
    matricula_aluno INT,
    email VARCHAR(100) NOT NULL,
    FOREIGN KEY (matricula_aluno) REFERENCES alunos(matricula_aluno),
    UNIQUE (matricula_aluno, email)
);

CREATE TABLE IF NOT EXISTS disciplinas (
    codigo_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    codigo_materia INT NOT NULL,
    semestre VARCHAR(6) NOT NULL, 
    vagas_maximas INT DEFAULT 60,  #define o padrão de vagas maximas como 60
    matricula_professor CHAR(4),
    FOREIGN KEY (codigo_materia) REFERENCES materias(codigo_materia),
    FOREIGN KEY (matricula_professor) REFERENCES professores(matricula_professor)
);

CREATE TABLE IF NOT EXISTS matriculas (
    matricula_aluno INT,
    codigo_disciplina INT,
    data_matricula DATE,
    situacao ENUM('cursando', 'aprovado', 'reprovado', 'trancado') DEFAULT 'cursando',
    PRIMARY KEY (matricula_aluno, codigo_disciplina),
    FOREIGN KEY (matricula_aluno) REFERENCES alunos(matricula_aluno),
    FOREIGN KEY (codigo_disciplina) REFERENCES disciplinas(codigo_disciplina)
);
