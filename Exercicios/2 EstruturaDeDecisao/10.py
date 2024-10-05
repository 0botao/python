# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def verificador(a):
    a = a.strip()

    if a == "":
        print("nao se pode deixar o espaço em branco")
    elif a not in ['M', 'V', 'N']:
        print("Caractere inválido. Digite M, V ou N.")
    else:
        return a

while True:

    turno = input(
'''
digite M para matutino 
digite V para vespertino
digite N para noturno \n
''')
    verificador(turno)
    if turno == 'M':
        print(' bom dia ')
    elif turno == 'V':
        print(' boa tarde ')
    elif turno == 'N':
        print('boa noite ')
