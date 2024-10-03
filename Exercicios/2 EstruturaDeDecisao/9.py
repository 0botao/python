# Faça um Programa que leia três números e mostre-os em ordem decrescente. 


def vazio(a):

    a = input(' digite um numero\n').strip()

    if a == '':
        print(' nao deixe o espaço em branco ')
    
    try:
        a = float(a)
        return a
    except ValueError:
        print('valor errado') 

while True:
    lista = []

    for i in range(3):
        numero = vazio(lista)
        lista.append(numero) 
    lista.sort()
    print(f' a lista de forma organizada é de {lista}')
