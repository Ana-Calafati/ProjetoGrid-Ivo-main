create database if not exists produto;
use produto;

CREATE table IF NOT EXISTS itens(
codigo int NOT NULL PRIMARY KEY,
produto varchar(50),
descricao varchar(50),
destaque bool,
valor varchar(200),
imagem varchar(300),
disponibilidade bool default 1
);

INSERT INTO itens (codigo, produto, descricao, destaque, valor, imagem) VALUES
(1, 'Hamburguer Revolução Francesa', 'Pra quem adora emoção', 0, "R$17,89", 'https://as1.ftcdn.net/v2/jpg/03/34/88/16/1000_F_334881645_vLmn5Hs1YyIYY1r0fcGGNAGZ0HL4ix8T.jpg'),
(2, 'Hamburguer Reforma Agrária', 'O agro é tudo', 1,  "R$18,18", 'https://as2.ftcdn.net/v2/jpg/04/42/34/69/1000_F_442346916_ALSQfu1lmjy1MA5sevWhuERbeTVc3BN7.jpg'),
(3, 'Hamburguer Fim do Capitalismo', 'A classe trabalhadora', 0, "R$23,12", 'https://as2.ftcdn.net/v2/jpg/03/03/11/75/1000_F_303117572_kZlWa7FDjRJXFdi7YoP17gPRCDmoI8Qt.jpg');

CREATE TABLE IF NOT EXISTS usuarios(
	usuario varchar(200) primary key,
    senha varchar(200) not null,
    nome varchar (100) default "anonimo"
);

SELECT * from usuarios;

CREATE TABLE IF NOT EXISTS carrinho(
	cod_carrinho int auto_increment primary key,
    usuario varchar(20),
    data datetime default current_timestamp,
    finalizado bool,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
    );
    
CREATE TABLE IF NOT EXISTS item_carrinho(
cod_item_carrinho int auto_increment primary key,
cod_carrinho int,
cod_produto int,
quantidade int default 1,
CONSTRAINT fk_itenscarrinho_carrinhos FOREIGN KEY (cod_carrinho) REFERENCES carrinhos (cod_carrinho),
CONSTRAINT fk_itenscarrinho_itens FOREIGN KEY (cod_produto) REFERENCES itens(codigo)
);