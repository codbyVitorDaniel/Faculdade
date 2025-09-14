/* CRIAR UMA BASE DE DADOS NOVA */
CREATE DATABASE aula;
/* DELETAR UMA BASE DE DADOS */
DROP DATABASE aula;
/* CRIO UMA DATABASE SE ELA EXISTIR */
CREATE DATABASE IF NOT EXISTS aula;
/* UTILIZAR UMA DATABASE EXISTENTE (ENETRAR NESSA DATABASE) */
USE aula;

/* CRIAR A NOSSA PRIMEIRA TABELA - ENTIDADE - ALUNO */
/*ID, NOME, IDADE*/

CREATE TABLE alunos(
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(100) NOT NULL,
idade INT NOT NULL
);
/* MOSTRA AS TABELAS CRIADAS */
SHOW TABLES;
/* DESCREVER UMA TABELA */
DESCRIBE alunos;
/* Inserir três valores na minha tabela alunos */
INSERT INTO alunos(nome, idade)
VALUES
("Vitor",32),
("Iago",20),
("Joao",19);
Drop table alunos; -- Apaga uma tabela

/* VISUALIZAR OS DADOS QUE ESTÃO NA MINHA TABELA*/
SELECT nome FROM alunos;



show tables; -- Monstra as tabelas existentes dentro de uma data base selecionada 


-- alterar a estrutura de uma tabela --> ALTER TABLE ADD

alter table alunos add column mail int; -- adiciona uma coluna 

alter table alunos drop column idade; -- exclue uma coluna

-- atera a estrutura de uma tabela -> ALTER TABLE MODIFY
alter table alunos modify column idade int not null;
-- where
select * from alunos;
select * from alunos
WHERE id = 1;

-- operadores logicos (and, or , not)
select * from alunos 
where id = 1 and nome = "Vitor"; -- 1. Duas condiçoes sejam verdadeiras 

select * from alunos
where id = 1 or nome = "Vitor"; -- 2 Resultados

select * from alunos
where not nome = "Vitor";


-- DELETE

Delete from alunos  -- NUNCA FAÇA EM PRODUÇAO
where id = "1" or id = "2"; -- NUNCA FAÇA DELETE SEM O WHERE


Delete from alunos  -- NUNCA FAÇA EM PRODUÇAO
delete from alunos
where id  = "3"; -- NUNCA FAÇA DELETE SEM O WHERE



select * from alunos;

-- UPDATE
update alunos
set email = "nao sei"; -- NUNCA FAÇA EM PRODUÇÂO 


update alunos
set email = "sei nao"
where id = 2;

-- ORDER BY
select * from alunos
order by id desc;

-- tem dois tipos um e esse => order by id asc; 
-- outro e esse => order by id desc;