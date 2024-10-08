# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% 
#para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220  

from tabulate import tabulate
def verificadorVazio(a):
    while True:
        a = a.strip()

        if a == "":
            print(' nao pode deixar o espaço em branco ')
            return None
        try:
            a = float(a)
            return a 
        except ValueError:
            print('erro de caracteres ')
            return None 
    
while True:
    horas = input(" digite as horas trabalhadas ?  \n")
    horas = verificadorVazio(horas) 

    money = input(" digite as horas trabalhadas ?  \n")
    money = verificadorVazio(money)

    salario = horas * money
    
    if salario is None:
        continue
    elif salario <= 0:
        print(' nao existe esse tipo de salario ')
    elif salario < 900:
        sinD = salario * 0.03
        fgts = salario * 0.11
        salario = salario - sinD
    elif salario < 1500:
        sinD = salario * 0.03
        fgts = salario * 0.11
        iR = salario * 0.05
        salarioLiquido = salario - (sinD + iR) 
    elif salario <= 2500:
        sinD = salario * 0.03
        fgts = salario * 0.11
        iR = salario * 0.10
        salarioLiquido = salario - (sinD + iR) 
    else: 
        sinD = salario * 0.03
        fgts = salario * 0.11
        iR = salario * 0.20
        salarioLiquido = salario - (sinD + iR) 

    tabela = [
        [f"Salário Bruto: {horas * money}", f"{salario}"],
        ["(-) IR (5%)", f"R$ {iR:.2f}"],
        ["(-) INSS (10%)", f"R$ {iR:.2f}"],
        ["FGTS (11%)", f"R$ {fgts}"],
        ["Total de descontos", f"R$ {salario-salarioLiquido}"],
        ["Salário Líquido", f"R$ {salarioLiquido:.2f}"]
    ]

    print(tabulate(tabela, headers=["Descrição", "Valor (R$)"], tablefmt="grid"))
