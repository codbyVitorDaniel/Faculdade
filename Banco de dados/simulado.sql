create DATABASE universidade;
use universidade;

CREATE TABLE alunos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome varchar(100) not null,
email varchar(90),
data_nacimento DATE NOT NULL,
cidade varchar(60)
);
-- Q1
ALTER TABLE alunos ADD COLUMN cidade VARCHAR(60) DEFAULT "Maricá";

-- Q2
ALTER TABLE cursos ADD COLUMN ativo TINYINT(1) DEFAULT 1;

-- Q3
UPDATE alunos SET cidade = "Maricá" 
WHERE cidade IS NULL OR cidade = "";


-- Q4
DELETE FROM matriculas WHERE aluno_id = 2 AND curso_id = 3;

-- Q5
SELECT id, nome, UPPER(nome) AS nome_maiusculo FROM alunos;

-- Q6
SELECT nome, TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) AS idade_anos 
FROM alunos ORDER BY idade_anos DESC;

-- Q7
SELECT DISTINCT cidade FROM alunos ORDER BY cidade ASC;

-- Q8
SELECT * FROM alunos WHERE nome LIKE ‘F%’;

-- Q9
SELECT nome, data_nascimento FROM alunos 
WHERE data_nascimento BETWEEN ‘1995-01-01’ AND ‘2000-12-31’;

-- Q10
SELECT COUNT(*) AS total FROM alunos 
WHERE TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) >= 25;

-- Q11
SELECT cidade, COUNT(*) AS total FROM alunos 
GROUP BY cidade ORDER BY total DESC;

-- Q12
SELECT cidade, COUNT(*) AS total FROM alunos 
GROUP BY cidade HAVING COUNT(*) >= 2;

-- Q13
INSERT INTO alunos (nome, data_nascimento, email) 
VALUES (‘Mariana Silva’, ‘2002-09-15’, ‘mariana@gmail.com’);

-- Q14
INSERT INTO cursos (nome, carga_horaria) VALUES (‘Administração’, 3600);

-- Q15
UPDATE cursos SET nome = ‘Direito Empresarial’ WHERE nome = ‘Direito’;

-- Q16
DELETE FROM cursos WHERE nome = ‘Engenharia de Produção’;

-- Q17
SELECT id, nome, email FROM alunos;

-- Q18
SELECT COUNT(*) AS total_alunos FROM alunos;

-- Q19
SELECT nome, data_nascimento FROM alunos
WHERE data_nascimento = (SELECT MIN(data_nascimento) FROM alunos)
   OR data_nascimento = (SELECT MAX(data_nascimento) FROM alunos);

-- Q20
SELECT AVG(carga_horaria) AS media_carga FROM cursos;

-- Q21
SELECT SUM(carga_horaria) AS soma_carga FROM cursos;

-- Q22
SELECT * FROM cursos WHERE carga_horaria BETWEEN 3700 AND 4500;

-- Q23
SELECT * FROM alunos WHERE id IN (1, 3, 5);

-- Q24
SELECT * FROM alunos WHERE nome LIKE ‘%o’;

-- Q25
SELECT YEAR(data_nascimento) AS ano, COUNT(*) AS total 
FROM alunos GROUP BY YEAR(data_nascimento);

-- Q26
SELECT YEAR(data_nascimento) AS ano, COUNT(*) AS total 
FROM alunos GROUP BY YEAR(data_nascimento) HAVING COUNT(*) >= 2;

-- Q27
SELECT nome, carga_horaria FROM cursos 