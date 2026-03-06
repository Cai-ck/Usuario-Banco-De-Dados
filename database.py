import asyncpg

async def conexao():
    try:
        return await asyncpg.connect(
            user='coloque seu usuário',
            password='coloque sua senha',
            host='localhost',
            port=5432,
            database='login_local' # nome da base de dados que você criou
        )
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None