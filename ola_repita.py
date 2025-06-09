  # Algoritmo "OLA" adaptado com estrutura equivalente a "repita ... até que"

# Declaração da variável que armazenará a escolha do usuário
opcao = -1  # Inicializado com valor qualquer diferente de 0

# Estrutura que simula "repita ... até que"
while True:
    # Exibe o menu de opções para o usuário
    print("----------------------")
    print("1 - Dizer olá!")
    print("2 - Dizer oi!")
    print("0 - Sair do programa")
    print("----------------------")

    # Lê a entrada do usuário
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        # Trata entradas inválidas que não podem ser convertidas para inteiro
        print("Entrada inválida. Digite um número.")
    else:
        # Verifica e executa a ação conforme a opção escolhida
        if opcao == 1:
            print("Olá!")
        elif opcao == 2:
            print("Oi!")
        elif opcao == 0:
            print("Saindo do programa...")
        else:
            print("Opção inválida. Tente novamente.")

    # Condição de parada no final do laço (simulando "até que opcao == 0")
    if opcao == 0:
        break  # Encerra o laço