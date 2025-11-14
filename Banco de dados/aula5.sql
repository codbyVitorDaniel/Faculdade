/*Trigger*/

/*
Um bloco de código SQL que é executado automaticamente
pelo banco de dados quando ocorre um determinado evento
(INSERT, UPDATE, DELETE) em uma tabela.
*/
/* Utilidade:
1 - Garantir a integridade de dados.
2 - Criar históricos de alterações(logs).
3 - Execucação de calculos automáticos.
4 - Enviar dados para outras tabelas(Espelhamento ou
auditoria).
*/

CREATE DATABASE aula_13_11;
USE aula_13_11;

CREATE TABLE produtos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
preco DECIMAL(10,2) NOT NULL,
estoque INT DEFAULT 0
);

CREATE TABLE log_produtos (
id INT AUTO_INCREMENT PRIMARY KEY,
produto_id INT,
acao VARCHAR(20),
data_acao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
valor_antigo DECIMAL(10,2),
valor_novo DECIMAL(10,2)
);

-- Criar um exemplo 1 - Trigger de auditoria em Update
DELIMITER $$
CREATE TRIGGER trg_auditoria_preco
AFTER UPDATE ON produtos
FOR EACH ROW
BEGIN
	IF OLD.preco <> NEW.preco THEN
		INSERT INTO log_produtos (produto_id, acao, valor_antigo, valor_novo)
        VALUES(OLD.id, 'ALTERACAO_PRECO', OLD.preco, NEW.preco);
	END IF;
END $$
DELIMITER ;

SHOW TRIGGERS;

SELECT * FROM produtos;
SELECT * FROM log_produtos;

INSERT INTO produtos(nome, preco, estoque)
VALUES("Notebook", 3500.00,10);

UPDATE produtos
SET preco = 3600.00
WHERE id = 1;

-- Exemplo prático 2 - Trigger Before Insert
DELIMITER $$
CREATE TRIGGER trg_valida_preco
BEFORE INSERT ON produtos
FOR EACH ROW
BEGIN
	IF NEW.preco < 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Preço não pode ser negativo';
	END IF;
END $$
DELIMITER ;

SHOW TRIGGERS;
INSERT INTO produtos(nome, preco, estoque)
VALUES("Teclado", -50, 20);

/*
Cria um trigger que salvar em uma tabela de
histórico o estoque.

update e insert
*/
/*Transação*/
/*
Uma transação é um conjunto de operações SQL
que devem ser executadas como uma unidade de
trabalho. De forma geral, ou tudo é executado
com sucesso, ou nada é aplicado.

Exemplos de situações que exigem transações:
1 - Transferência de dinheiro entre contas.
2 - Atualizações em múltiplas tabelas
relacionadas.
3 - Processos críticos que não podem ficar pela
metade.
*/
/* ACID - Propriedades
A - Atomicidade: Todas as operações da transação
são executadas completamente ou nenhuma é.
C - Consistência: O banco permanece em um estado
válido, antes e depois da transação.
I - Isolamento: Transações não interferem umas nas
outras.
D - Durabilidade: Após o COMMIT, as mudanças são
permanentes mesmo após a falha.
*/
-- Comandos
/*
START TRANSACTION: Inicia uma nova transação.
COMMIT: Confirma as operações da transação.
ROLLBACK: Cancela as operações realizadas desde o
último commit ou savepoint.
SAVEPOINT nome: Cria um ponto de restauração dentro
da transação.
ROLLBACK TO nome: Retorna ao ponto definido pelo
SAVEPOINT.
*/
CREATE DATABASE bancoAula;
USE bancoAula;

CREATE TABLE contas(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50),
saldo DECIMAL(10,2)
);
INSERT INTO contas(nome, saldo)
VALUES
("Fabricio", 1000.00),
("José", 500.00);

-- INICIA A TRANSAÇÃO
START TRANSACTION;

-- 1. Retirada de R$200,00 da conta do Fabricio
UPDATE contas
SET saldo = saldo -200
WHERE nome = "Fabricio";
SAVEPOINT ponto1;

-- 2. Adicionar R$200,00 na conta do José
UPDATE contas
SET saldo = saldo + 200
WHERE nome = "José";
-- Se tudo deu certo
SAVEPOINT ponto2;

COMMIT;

ROLLBACK TO ponto1;

SELECT * FROM contas;