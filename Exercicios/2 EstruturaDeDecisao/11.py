# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento. 


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
    salario = input(' digite  o seu salario \n')
    salario = verificadorVazio(salario)

    if salario is None:
        continue
    elif salario <= 0:
        print(' não existe esse tipo de salario ')
    elif salario <= 280:
        print(f'o seu salario antigo era de R${salario:.2f}, o seu novo salario é de R${(salario + (salario*0.20)):.2f} com um aumento de 20%')
    elif salario <= 700:
        print(f'o seu salario antigo era de R${salario:.2f}, o seu novo salario é de R${(salario + (salario*0.15)):.2f}, com um aumento de 15% ')
    elif salario <= 1500:
        print(f'o seu salario antigo era de R${salario:.2f}, o seu novo salario é de R${(salario + (salario*0.10)):.2f}, com um aumento de 10%')
    else:
        print(f'o seu salario antigo era de R${salario:.2f}, o seu novo salario é de R${(salario + (salario*0.05)):.2f}, com um aumento de 5%')
