def validar_cpf(cpf):
    """
    Valida um número de CPF.

    Args:
        cpf (str): O CPF a ser validado (pode conter pontos e hifens).

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    # Remove caracteres não numéricos (pontos, hifens, espaços)
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11), o que o torna inválido
    if cpf == cpf[0] * 11:
        return False

    # Validação do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto
    if digito_1 != int(cpf[9]):
        return False

    # Validação do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto
    if digito_2 != int(cpf[10]):
        return False

    return True

# --- Exemplos de uso ---
print("--- Testes de Validação ---")

# CPFs válidos (exemplos - não são CPFs reais)
cpf_valido_1 = "123.456.789-09" # Exemplo válido
cpf_valido_2 = "98765432100"   # Exemplo válido
print(f"'{cpf_valido_1}' é válido? {validar_cpf(cpf_valido_1)}")
print(f"'{cpf_valido_2}' é válido? {validar_cpf(cpf_valido_2)}")

# CPFs inválidos
cpf_invalido_1 = "123.456.789-00" # Dígito verificador incorreto
cpf_invalido_2 = "111.111.111-11" # Todos os dígitos iguais
cpf_invalido_3 = "123.456.789-0"  # Menos de 11 dígitos
cpf_invalido_4 = "00000000000"   # Todos os dígitos iguais (outro exemplo)
cpf_invalido_5 = "123456789012"  # Mais de 11 dígitos
print(f"'{cpf_invalido_1}' é válido? {validar_cpf(cpf_invalido_1)}")
print(f"'{cpf_invalido_2}' é válido? {validar_cpf(cpf_invalido_2)}")
print(f"'{cpf_invalido_3}' é válido? {validar_cpf(cpf_invalido_3)}")
print(f"'{cpf_invalido_4}' é válido? {validar_cpf(cpf_invalido_4)}")
print(f"'{cpf_invalido_5}' é válido? {validar_cpf(cpf_invalido_5)}")

# Exemplo de interação com o usuário
print("\n--- Interação com o Usuário ---")
cpf_digitado = input("Digite um CPF para validar: ")
if validar_cpf(cpf_digitado):
    print(f"O CPF '{cpf_digitado}' é VÁLIDO!")
else:
    print(f"O CPF '{cpf_digitado}' é INVÁLIDO!")