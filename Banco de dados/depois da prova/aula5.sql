CREATE DATABASE aula_06_11;
USE aula_06_11;

/*Subquery*/

/* Uma consulta dentro de outra consulta.

Ela serve para retornar dados intermediários para a consulta
principal.

IN, EXISTS, = , >, <
*/
/*Tipos de subquery*/

/*
1 - Escalar(Retorna um único valor)
EX: (SELECT MAX(preco) FROM produtos);

2 - De linha - Retorna um único valor ou uma linha única
Ex: (SELECT AVG(salario) FROM funcionarios);

3 - De múltiplos valores(linhas) Retorna vários valores
EX: IN (SELECT id FROM clientes WHERE cidade = "Maricá");

4 - Correlacionada - Depende de uma consulta externa
Ex:

WHERE salario >
(SELECT AVG(salario)
FROM funcionarios f2
WHERE f2.departamento = f1.departamento)
*/
-- Clientes
-- Produtos
-- Pedidos
-- Itens de Pedido


CREATE TABLE clientes(
id INT primary key auto_increment,
nome VARCHAR(100) NOT NULL,
cidade VARCHAR(90) NOT NULL
);

CREATE TABLE produtos(
id INT primary key auto_increment,
nome VARCHAR(100) NOT NULL,
preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE pedidos(
id INT primary key auto_increment,
id_cliente INT,
data_pedido DATE DEFAULT (CURDATE()),
FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

CREATE TABLE itens_pedido(
id INT primary key AUTO_INCREMENT,
id_produto INT,
id_pedido INT,
quantidade INT,
FOREIGN KEY (id_produto) REFERENCES produtos(id),
FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
);

INSERT INTO clientes(nome, cidade)
VALUES
("Ana","Maricá"),
("Bruno","Niterói"),
("Diego","São Gonçalo"),
("Giovanna","Maricá"),
("Juan","Niterói");

INSERT INTO clientes(nome, cidade)
VALUES
("Camila","Maricá");


INSERT INTO produtos(nome, preco)
VALUES
("Teclado",120.00),
("Mouse",60.00),
("Monitor",250.00),
("Cadeira Gamer",1200.00);

INSERT INTO pedidos(id_cliente, data_pedido)
VALUES
(2,"2025-02-12"),
(4,"2025-07-20");

INSERT INTO pedidos(id_cliente)
VALUES
(1),
(3),
(5);

INSERT INTO itens_pedido(id_pedido, id_produto, quantidade)
VALUES
(1,1,2),
(1,2,1),
(2,3,1),
(3,4,1),
(4,2,3);

select * from itens_pedido;

-- Consulta Básica
-- Total de clientes por cidade
SELECT cidade, COUNT(*) AS total_clientes
FROM clientes
GROUP BY cidade;

-- Produto mais caro do que R$ 500,00
SELECT nome, preco
FROM produtos
WHERE preco > 500;

-- Subquery no Where
-- Listar os produtos com o preco acima da média
SELECT nome, preco
FROM produtos
WHERE preco > (SELECT AVG(preco) FROM produtos);

SELECT AVG(preco) FROM produtos;
SELECT nome, preco FROM produtos;

SELECT nome, preco
FROM produtos
WHERE preco > 407.50;

-- Liste o nome dos clientes que fizeram pedido -- IN
SELECT nome
FROM clientes
WHERE id IN (SELECT id_cliente FROM pedidos);


-- Liste o nome dos clientes que NÂO fizeram pedido -- IN
SELECT nome
FROM clientes
WHERE id NOT IN (SELECT id_cliente FROM pedidos);