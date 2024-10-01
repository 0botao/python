# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
#  total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
#  5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo: 

while True:
    try:
        salario = float(input(' digite o seu salario bruto \n'))
    except ValueError as e:
        print(f"erro, {e} é um caractere invalido ") 
    
    print(f"""
inss: {(salario - (salario * 0.08)):.2f} \n
sindicato: {(salario - (salario * 0.05)):.2f} \n
imposto de renda: {(salario - (salario * 0.11)):.2f} \n
salario liquido: {(salario - (salario * 0.24)):.2f} \n
""")
    

