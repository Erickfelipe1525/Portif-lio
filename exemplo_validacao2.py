def validar_nome(nome):
    # Verifica se todos os caracteres do  nome são letras
    if nome.isalpha():
        return True
    else:
        return False
    
def validar_idade(idade):
    # Verifica se todos os caracteres da idade são dígitos
    if idade.isdigit():
        return True
    else:
        return False
    
# Solicita ao usuário que insira um nome
nome = input("Digite seu nome: ")
# Solicita ao usuário que insira uma idade
idade = input("Digite sua idade: ")

# Valida o nome usado a função validar_nome
if validar_nome(nome):
    print("Nome válido!")
else:
    print("Nome inválido! O nome deve conter apenas letras.")

# Valida a idade usando a função validar_idade
if validar_idade(idade):
    print("Idade válida!")
else:
    print("Idade inválida! O nome deve conter apenas números.")