import mysql.connector

def obter_conexao():
    try:
        return mysql.connector.connct(
            host = "localhost",
            user = "Adicionar Usuario",
            password = "Adicionar senha",
            database = "login_local",
            allow_public_key_retrieval = True,
            use_ssl = False
        )
    except mysql.connector.Error as err:
     print(f"Erro de conexão: {err}")    
     return None