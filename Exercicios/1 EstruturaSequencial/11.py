# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro. 
# o terceiro elevado ao cubo.

def adicionar(a, b):
    a.append(b)
    return a


lista = []

try:
    while True:
        for i in range(2):
            while True:
                try:
                    numero = int(input("Digite um número inteiro: "))
                    lista = adicionar(lista, numero)
                    break 
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro.")
        while True:
            try:
                floturante = float(input("Digite um número real: "))
                lista = adicionar(lista, floturante)
                break 
            except ValueError:
                print("Entrada inválida. Por favor, digite um número real.")
        break  
except ValueError:
    print("Ocorreu um erro inesperado.")
else:
    print(f''' 
        O  produto do dobro do primeiro com metade do segundo é {(lista[0] *2) + (lista[1])},
        a soma do triplo do primeiro com o terceiro {lista[0] * 2 + lista[2] },
        o terceiro elevado ao cubo {lista[2]**3}
    ''''')
    print("Os números digitados foram adicionados à lista:", lista)
