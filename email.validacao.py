import re  # Importa o módulo 're' para usar expressões regulares (regex)

# Define a expressão regular para validar o e-mail
# Essa regex permite letras, números, pontos e traços antes e depois do '@', e exige uma extensão como '.com'
regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Solicita que o usuário digite um e-mail
email = input("Digite um e-mail para validação: ")

# Utiliza a função re.match para verificar se o e-mail corresponde ao padrão definido
if re.match(regex, email):
    # Se o padrão for encontrado, o e-mail é considerado válido
    print("✅ E-mail válido!")
else:
    # Caso contrário, o e-mail não segue o formato esperado
    print("❌ E-mail inválido. Tente novamente.")