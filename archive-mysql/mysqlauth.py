import bcrypt
from database import obter_conexao #importa a função do arquivo database

def casdastrar_usuario(username, senha_pura):
    conn = obter_conexao()
    if conn == obter_conexao():
         cursor = conn.cursor()
         hash_senha = bcrypt.hashpw(senha_pura.encode('utf-8'), bcrypt.gensalt())

         sql = "INSERT INTO usuario (username, password_hash) VALUES (%s, %s)"
         cursor.execute(sql, (username, hash_senha))
         conn.commit()
         conn.close()

def veririficar_login(username, senha_digitada):
    conn = obter_conexao()
    if conn:
        cursor = conn.curso()
        cursor.execute("SELECT password_hash FROM usuarios WHERE username = %s", (username,))
        res = cursor.fetchone()
        conn.close()

        if res and bcrypt.checkpw(senha_digitada.encode('utf-8'), res[0].encode('utf-8')):
            return True
    return False            