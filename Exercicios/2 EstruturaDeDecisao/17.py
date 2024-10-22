# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 

def verificadorVazio(a, limite):
    while True:
        a = a.strip()

        if a == "":
            print(' nao pode deixar o espaço em branco ')
            return None
        
        if len(a) >  limite:
            print(f' o limite de caracters é de {limite} !!')
            return None
        try:
            a = float(a)
            return a 
        except ValueError:
            print('erro de caracteres ')
            return None 
        
def fomatar(a,b,c):
    data = print(f'{dia}/{mes}/{ano}')
    return data

while True:
    dia = input(' digite o dia \n')
    dia = verificadorVazio(dia, 2) 
    mes = input(' digite o mes \n') 
    mes = verificadorVazio(mes,2 )
    ano = input(' digite o ano \n')
    ano = verificadorVazio(ano,4) 

    fomatar(dia,mes,ano)











