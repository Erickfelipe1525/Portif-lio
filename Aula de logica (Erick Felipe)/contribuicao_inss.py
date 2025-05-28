salario_contribuicao = float(input("Digite o salário de contribuição"))

if salario_contribuicao <= 1692.72:

         contribuicao_inss = salario_contribuicao * 0.08

elif salario_contribuicao >= 1692.73 and salario_contribuicao <= 2822.90:
        
        contribuicao_inss = salario_contribuicao * 0.09

elif salario_contribuicao >= 2822.90 and salario_contribuicao <= 5645.90:
        
        contribuicao_inss = salario_contribuicao * 0.11


print (f"A Contribuição do INSS: R$ {contribuicao_inss:.2f}")