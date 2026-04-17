import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password= "root",
                    database= "produto"
            )
              
            #criando cursor
    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor


def salvar_no_banco(nome, senha):
    # Estabelece a conexão
    conexao = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco"
    )
    cursor = conexao.cursor()

    # O comando SQL para inserir
    sql = "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)"
    valores = (nome, senha)

    cursor.execute(sql, valores)
    conexao.commit() # Salva as alterações
    
    cursor.close()
    conexao.close()