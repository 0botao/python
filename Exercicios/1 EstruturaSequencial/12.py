# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 

while True:
    try:
        altura = float(input(f" digite a sua altura "))
        peso = float(input(f" digite o seu peso ")) 
        while True:
            s = input("digite F para feminino e M para masculino")
            if s.upper == "M":
                print(f" o  seu peso e altura idela é de {(72.7*h) - 58} ")
                
            elif s.upper == "F":
                (f" o seu peso ideal e {(62.1*altura) - 44.7}")
                
            else:
                print("caractere invalido")
                break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número real.")
    else:
        print()
        break