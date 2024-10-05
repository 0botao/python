# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E 

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

def verEntradaValida(a):
    print

while True:
    while True:
        nota1 = input(' digite a sua primeira nota ')
        nota1 = verificadorVazio(nota1) 
        if nota1 is not None:
            break
    while True:
        nota2 = input(' digite a sua segunda  nota ')
        nota2 = verificadorVazio(nota2)
        if nota2 is not None:
            break
    
    if (nota1 + nota2) /2  <= 0 :
        print(' notas incorretas ') 
    elif (nota1 + nota2) /2  <= 4:
        print(' E ') 
    elif (nota1 + nota2) / 2 < 6:
        print(' D ') 
    elif (nota1 + nota2) / 2 < 7.5:
        print(' C ') 
    elif (nota1 + nota2) / 2 < 9 :
        print(' B ') 
    elif (nota1 + nota2) / 2 <= 10:
        print('A ')
    else:
        print(' nota invalida ')



