-- Group by Agrupar registros de acordo com um ou mais campos
SELECT * FROM alunos;
select YEAR(data_nascimento) as "Ano de Nascimento",
COUNT(*) as "Quantidade de alunos por ano"
FROM alunos;
Group by year (data_nascimento)
having COUNT(*) >= 2;

-- Contagem dos alunos nascidos depois de 1995.
SELECT YEAR(data_nascimento) AS ano, COUNT(*) Quantidade
FROM alunos

WHERE YEAR(data_nascimento) > 1995
GROUP BY (data_nascimento);

-- contagem com order by 

SELECT YEAR(data_nascimento) AS ano, COUNT(*) Quantidade
FROM alunos

WHERE YEAR(data_nascimento) > 1995
GROUP BY (data_nascimento);


/*
Having x WHere
where: Filtrar Linhas antes de agrupar
having: Filtrar apos o agrupamento
*/
-- Alunos Nascidos entre 1995 - 2000
-- Year & Between

SELECT year(data_nascimento) AS ano, COUNT(1995 - 2000) Quantidade

FROM Alunos
WHERE YEAR (data_nascimento) BETWEEN 1995 AND 2000;

-- Agrupar todos os registros de matricula por cursor e monstrar quantos alunos cada curso tem

/* joins 
os */

select from matriculas;
select from curso;
select from matriculas;

insert INTO matriculas(id_alunos,id_curso)
VALUES
(2,3),
(3,1),
(4,2),
(5,4),
(1,3);

SELECT alunos.nome AS "Nome dos alunos",
alunos.data_nascimento AS "DATA de Nascimento",
cursos.nome AS "Curso Matriculado";
matriculas.data_matriculas AS "Data da Matricula do Aluno"
FROM alunos 
INNER JOIN matriculas ON alunos.id = matriculas.id_alunos
INNER JOIN cursos ON cursos.id = matriculas.id_cursos;

--Inner join com alias

SELECT alunos.nome AS "Nome dos alunos",
a.data_nascimento AS "DATA de Nascimento",
c.nome AS "Curso Matriculado";
m.data_matriculas AS "Data da Matricula do Aluno"
FROM alunos a
INNER JOIN matriculas m ON alunos.id = m.id_alunos
INNER JOIN cursos  c ON c.id = m.id_cursos;
