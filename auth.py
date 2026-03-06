import bcrypt as bc
from database import conexao

async def cadastrar_usuario(nome, senha):
    conn = await conexao()
    if conn is None:
        return False

    try:
        # Hash da senha
        hashed_password = bc.hashpw(senha.encode('utf-8'), bc.gensalt())

        # Inserir o novo usuário no banco de dados
        await conn.execute(
            "INSERT INTO usuarios (username, password_hash) VALUES ($1, $2)",
            nome, hashed_password.decode('utf-8')
        )
        print("Usuário cadastrado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return False
    finally:
        await conn.close()
        
async def autenticar_usuario(nome, senha):
    conn = await conexao()
    if conn is None:
        return False

    try:
        # Buscar o usuário no banco de dados
        row = await conn.fetchrow(
            "SELECT password_hash FROM usuarios WHERE username = $1",
            nome
        )
        
        if row is None:
            print("Usuário não encontrado.")
            return False
        
        stored_hashed_password = row['password_hash'].encode('utf-8')

        # Verificar a senha
        if bc.checkpw(senha.encode('utf-8'), stored_hashed_password):
            print("Autenticação bem-sucedida.")
            return True
        else:
            print("Senha incorreta.")
            return False
    except Exception as e:
        print(f"Erro ao autenticar usuário: {e}")
        return False
    finally:
        await conn.close()