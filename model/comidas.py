from database.conexao import conectar

def mostrar_comidas():
    conexao, cursor = conectar()

    #executado consulta genero
    cursor.execute("SELECT codigo, produto, descricao, destaque, valor, imagem, disponibilidade FROM itens;")

    #recuperando os dados do genero
    item = cursor.fetchall()

    #Fechando
    conexao.close()

    return item