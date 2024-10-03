# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

while True:
    numero = input(" digite um numero ").strip()

    if numero == "":
        print(" digite um numero valido ") 
        continue 

    try:
        numero = float(numero)
        if numero >= 0 :
            print(" é um numero positivo ")
        else:
            print( " é um numero negativo")

    except ValueError:
        print(" digite um caractere valido ")

