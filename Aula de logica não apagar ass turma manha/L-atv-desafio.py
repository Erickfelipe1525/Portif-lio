def main():
    nome = ""
    idade = 0
    opcao = 0
    while True:
        print("   [MENU PRINCIPAL]")
        print("1.Cadastro de usuario")
        print("2.Ver cadastro")
        print("3.Sair do Sistema")
        print("-----------------")
        opcao=int(input("Escolha uma opção: "))
        if opcao == 1:
            nome=input("Digite seu nome: ")
            idade=int(input("Digite sua idade: "))
            print("Cadastro Concluido")
        elif opcao == 2:
            if nome == "" or idade == 0:
                print ("Nenhum dado Cadastrado")
            else:
                print("   [Dados cadastrados]")
                print(f"Nome:{nome}")
                print(f"Idade:{idade} anos")

        elif opcao == 3:
         print("Encerrando o Sistema...")
         break
        else:
            print("Opção invalida")

if __name__=="__main__":
    main()