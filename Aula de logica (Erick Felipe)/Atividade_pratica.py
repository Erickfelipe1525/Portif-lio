# Leitura do número
numero = input("Digite um número inteiro: ")

# Verificação se é palíndromo
if numero == numero[::-1]: # fatiamento (slice), [início:fim:passo]
# :: Não colocamos início nem fim, então pegamos toda a string.
# -1, ou seja, anda de trás para frente.
    
    print("O número {numero} é um palíndromo!")
else:
    print("O número {numero} não é um palíndromo.")
