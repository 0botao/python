# Faça um Programa que leia três números e mostre o maior e o menor deles. 

def verificador():
    while True:
        a = input(' digite um numero   \n').strip()

        if a == "":
            print(" n1 nao pode ser usado ")
            continue

        try:
            a = float(a)

            return a
        except ValueError:
            print("entrada do n1 invalida ") 
while True:

    numero1 = verificador()  
    numero2 = verificador()
    numero3 = verificador()
    
    if numero1 > numero2 and numero1 > numero3:
        print(f' o numero {numero1} é maior de todos')
    elif numero2 > numero1 and numero2 > numero3:
        print(f' o numero {numero3} é  maior de todos ')
    elif numero3 > numero1 and numero3 > numero2:
        print(f'o numero {numero3} é maior de todos')
    else:
        print()
