# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido 

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
    dia = input('''
Digite o dia da semana confrome os numeros apresentados abaixo
1 - domingo 
2 - segunda
3 - terça
4 - quarta
5 - quinta
6 - sexta
6 - sabado
''') 

    dia = verificadorVazio(dia) 

    if dia is None:
        continue
    elif dia <= 0 or dia > 7:
        print(' valor invalido') 
    elif dia == 1:
        print(' domingo ')
    elif dia == 2:
        print(' segunda ')
    elif dia == 3:
        print(' terça ')
    elif dia == 4:
        print(' quarta')
    elif dia == 5:
        print(' quinta ')
    elif dia == 6:
        print(' sexta ')
    else:
        print(' sabado')