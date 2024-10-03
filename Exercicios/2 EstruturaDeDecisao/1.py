# Faça um Programa que peça dois números e imprima o maior deles. 

while True:
    while True:
        n1 = input(' digite um numero para o n1  \n').strip()

        if n1 == "":
            print(" n1 nao pode ser usado ")
            continue

        try:
            n1 = float(n1)
            break
        except ValueError:
            print("entrada do n1 invalida ") 

    while True:
        n2 = input(' digite um numero para o n2  \n').strip()

        if n2 == "":
            print(" n2 nao pode ser usado ")
            continue

        try:
            n2 = float(n2)
            break
        except ValueError:
            print("entrada do n1 invalida ") 

    if n1 > n2:
        print(f" o numero {n1} é maior que o o numero {n2} \n") 
    elif n1 < n2 :
        print(f" o numero {n2} é maior que  o numero {n1} \n")
    else:
        print(" os numeros sao iguais ")