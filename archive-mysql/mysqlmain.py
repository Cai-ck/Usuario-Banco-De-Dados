def exibir_cabecalho():
    print("-" * 40)
    print("      GAJ - Gerenciador de Jogos      ")
    print("      (Acervo Local de Jogos)        ")
    print("-" * 40)

def menu_principal():
    while True:
        limpar_tela()
        exibir_cabecalho()
        print("\n[1] Criar Nova Conta")
        print("[2] Entrar no Sistema")
        print("[3] Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            user = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            cadastrar_usuario(user, senha)
            input("\nPressione Enter para voltar...")
            
        elif opcao == "2":
            user = input("Usuário: ")
            senha = input("Senha: ")
            if verificar_login(user, senha):
                input(f"\nSucesso! Bem-vindo ao GAJ, {user}. [Enter para continuar]")
                # Aqui você chamará o módulo de biblioteca novamente
            else:
                input("\nFalha no login. Tente novamente...")
                
        elif opcao == "3":
            print("Saindo... Até a próxima!")
            break
        else:
            input("Opção inválida! [Enter]")