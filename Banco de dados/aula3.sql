CREATE DATABASE universidade;
USE universidade; 
/* 3- TABELAS 
1 - ALUNOS
2- CURSOS
3 - MATRICULAS (ID_ALUNOS, ID_CURSO)
*/

CREATE TABLE alunos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(90) NOT NULL,
data_nascimento DATE NOT NULL 
);
CREATE TABLE cursos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(90) NOT NULL,
carga_horaria INT NOT NULL
);

CREATE TABLE matriculas(
id INT AUTO_INCREMENT PRIMARY KEY,
id_aluno INT,
id_curso INT,
nome VARCHAR(20),
cursos VARCHAR(20),
carga_horaria INT,
data_matricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_aluno) REFERENCES alunos(id),
FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

SHOW TABLES;
DROP TABLES nova_tabela;

/*Inserir 5 nomes em alunos
Inserir 4 cursos
Engenharia de Software - 3600
Direito - 4200
*/
create table nova_tabela(
nome VARCHAR(20),
cursos VARCHAR(30),
carga_horaria INT
);

insert into nova_tabela(nome, carga_horaria, cursos)
values
("Vitor",3600,"Engenharia de Software"),
("Isabele",4200,"Direito"),
("Ana",3600,"Engenharia de Software"),
("carol",3600,"Engenharia de Software");
select * from  nova_tabela;


/*
-- funçoes  
*/

-- funções - Vão ajudar a realizar operações de forma simples e rápida
-- Count -> Contar elementos 
select * from alunos;
select COUNT(*) as "Total de Alunos"
FROM alunos
-- Contem o total de cursos cadastrados
select Count(*) as "Total de cursos"
from cursos;
--Função MIN - MEnor valor 
-- Retonar o alunos mais velho
select MIN (id) AS "Menor id cadastrado"
FROM alunos;

SELECT MAX(id) AS "Maior id cadastrado"
FROM alunos;

--Menor carga_horaria do curso 
SELECT MIN(carga_horaria) AS "Menor carga horaria"
FROM cursos;
--Media -> carga horaria -> cursos
SELECT AVG(carga_horaria) AS "Media de carga horaria"
FROM cursos;
--Soma -> Total de carga horaria dos cursos
SELECT SUM(carga_horaria) AS "Soma de carga horaria"
FROM cursos;
--Between, in , like
-- quero selecionar as cargas horarias entre 4100 e 4700
SELECT nome, carga_horaria
FROM cursos
WHERE carga_horaria BETWEEN 4100 AND 4700;

-- In -> usado para verificar se um valor esta dentro de uma lista
select id, nome
from alunos
where id in (1,2,3);

-- LIKE
-- FILTRAR POR ESPECIFICAÇOES(NOMES QUE COMECE COM A LETRA F)
SELECT nome
FROM alunos
WHERE nome like "F%";

--FILTRAR NOMES QUE TERMINAM COM A LETRA A
SELECT nome
FROM alunos
WHERE nome LIKE "%S";

