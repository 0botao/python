# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão 
# é sempre pelo mais barato.

def verificador():
    while True:
        a = input(' digite o preço do produto  \n').strip()

        if a == "":
            print(" preço digitado incorretamente ")
            continue

        try:
            a = float(a)

            return a
        except ValueError:
            print("entrada invalida ") 
while True:

    numero1 = verificador()  
    numero2 = verificador()
    numero3 = verificador()
    
    if numero1 < numero2 and numero1 < numero3:
        print(f' o produto {numero1} é mais barato  de todos')
    elif numero2 < numero1 and numero2 < numero3:
        print(f' o produto {numero3} é  o mais barato de todos ')
    elif numero3 < numero1 and numero3 < numero2:
        print(f'o produto {numero3} é o mais barato de todos')
    else:
        print()
