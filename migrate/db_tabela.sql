create database if not exists produto;
use produto;

CREATE table IF NOT EXISTS itens(
codigo int NOT NULL PRIMARY KEY,
produto varchar(50),
descricao varchar(50),
destaque bool,
valor float,
imagem varchar(300)
);

INSERT INTO itens (codigo, produto, descricao, destaque, valor, imagem) VALUES
(1, 'Notebook', 'Notebook 16GB RAM', true, 3500.00, 'notebook.jpg'),
(2, 'Smartphone', 'Celular 128GB', false, 1800.50, 'smartphone.jpg'),
(3, 'Fone Bluetooth', 'Fone sem fio', true, 250.99, 'fone.jpg'),
(4, 'Mouse Gamer', 'Mouse RGB 7200 DPI', false, 120.75, 'mouse.jpg'),
(5, 'Teclado Mecânico', 'Teclado ABNT2', true, 300.00, 'teclado.jpg');