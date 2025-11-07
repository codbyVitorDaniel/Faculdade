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

/* Subquery no FROM (subconsulta com tabela)
 Liste a quantidade total vendida
 utilizando uma subconsulta para calcular o total de
 cada produto primeiro
*/

SELECT p.nome, sub.total_vendido
FROM(
	SELECT id_produto, SUM(quantidade) AS total_vendido
    FROM itens_pedido
    GROUP BY id_produto
) AS sub
JOIN produtos p ON p.id = sub.id_produto;

SELECT id_produto, SUM(quantidade) AS total_vendido
FROM itens_pedido
GROUP BY id_produto;

-- Subquery correlacionada
-- Liste o nome dos produtos cujo preço é maior do que a média
-- dos produtos do mesmo pedido.

SELECT p.nome
FROM produtos p
WHERE preco > (
	SELECT AVG(p2.preco)
    FROM produtos p2
    WHERE p2.id <> p.id
);

-- Mostre as cidades com números de pedidos acima da média geral
-- de pedidos por cidade

SELECT c.cidade, COUNT(p.id) AS total_pedidos
FROM clientes c
JOIN pedidos p ON p.id_cliente = c.id
GROUP BY c.cidade
HAVING COUNT(p.id) > (
	SELECT AVG(total)
    FROM(
    SELECT COUNT(p2.id) AS total
    FROM clientes c2
    JOIN pedidos p2 ON p2.id_cliente = c2.id
    GROUP BY c2.cidade
    ) AS sub
);

SELECT c.cidade, COUNT(p.id) AS total_pedidos
FROM clientes c
JOIN pedidos p ON p.id_cliente = c.id
GROUP BY c.cidade;
CREATE DATABASE IF NOT EXISTS loja;
USE loja;

CREATE TABLE clientes(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(60) NOT NULL,
cidade VARCHAR(50) NOT NULL,
criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pedidos(
id INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT,
valor_total DECIMAL(10,2),
data_pedido DATE,
FOREIGN KEY(id_cliente) REFERENCES clientes(id)
);

INSERT INTO clientes(nome, cidade)
VALUES
("Ana","Maricá"),
("Bruno","Niterói"),
("Camile","Itaboraí");

INSERT INTO pedidos(id_cliente, valor_total, data_pedido)
VALUES
(1,150.00,'2024-10-01'),
(1,80.00,'2024-10-15'),
(2,250.00,'2025-10-20'),
(3,70.00,'2025-01-12');

/*STORED PROCEDURE*/

/*
É um conjunto de comandos SQL armazenados no servidor de banco de dados
Ela é criada uma vez e pode ser executada várias vezes, facilitando a
automação
*/

/* Principais Vantagens de
1 - Reutirlização de Código
2 - Melhor Performance(Executa no servidor, não precisa enviar
vários comandos)
3 - Segurança(controle total de acesso e encapsulamento da
lógica de negócio)
4 - Padronização das operações complexas
*/

-- Criar a nossa primeira procedure
-- Listar os clientes

DELIMITER $$

CREATE PROCEDURE listar_clientes()
BEGIN
	SELECT * FROM clientes;
END $$

DELIMITER ;

CALL listar_clientes();

-- Procedure com parâmetros de entrada
DELIMITER $$

CREATE PROCEDURE pedidos_por_cliente(IN idBusca INT)
BEGIN
	SELECT c.nome, p.valor_total, p.data_pedido
    FROM clientes c
    JOIN pedidos p ON c.id = p.id_cliente
    WHERE c.id = idBusca;
END $$

DELIMITER ;
CALL pedidos_por_cliente(1);

-- Procedure com parâmetros de saída
DELIMITER $$

CREATE PROCEDURE total_clientes(IN idCliente INT, OUT total DECIMAL(10,2))
BEGIN
	SELECT SUM(valor_total) INTO total
    FROM pedidos
    WHERE id_cliente = idCliente;
END $$

DELIMITER ;

CALL total_clientes(1, @resultado);
SELECT @resultado AS total_do_cliente_1;



DELIMITER $$

CREATE PROCEDURE verificar_compras(IN idcliente INT)
BEGIN
	DECLARE totalPedidos INT;
    
    SELECT COUNT(*) INTO totalPedidos
    FROM pedidos
    WHERE id_cliente = idcliente;
    
    IF totalPedidos > 0 THEN
		SELECT CONCAT('O cliente possui ', totalPedidos, ' pedidos.') AS mensagem;
	ELSE
		SELECT 'O cliente não possui pedidos' AS mensagem;
	END IF;
END $$

DELIMITER ;

CALL verificar_compras(1);

DROP PROCEDURE IF EXISTS verificar_compras;