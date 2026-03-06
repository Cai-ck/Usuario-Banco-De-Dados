import asyncio
import database
import auth

print("Bem-vindo a plataforma GAJ!")
print("1. Cadastrar usuário")
print("2. Autenticar usuário")

opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == '1':
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    asyncio.run(auth.cadastrar_usuario(nome, senha))
elif opcao == '2':
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    asyncio.run(auth.autenticar_usuario(nome, senha))
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")