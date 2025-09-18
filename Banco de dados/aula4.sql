-- Group by Agrupar registros de acordo com um ou mais campos
SELECT * FROM alunos;
select YEAR(data_nascimento) as "Ano de Nascimento",
COUNT(*) as "Quantidade de alunos por ano"
FROM alunos;
Group by 