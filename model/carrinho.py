from database.conexao import conectar

def recuperar_carrinho(usuario: str) -> list:
    conexao, cursor = conectar()
    cursor.execute(""" SELECT 
                    """)
    recuperar = cursor.fetchall()
    conexao.close()
    return recuperar