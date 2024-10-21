# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 

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
    dia = input(' digite o dia \n')
    dia = verificadorVazio(dia) 
    mes = input(' digite o mes \n') 







