# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
 
inteiro = int(input(" digite um numero inteiro \n"))
numeroReal1 = float(input(" digite o primeiro numero real \n"))
numeroReal2 = float(input(" digite o segundo numerio real "))

print(
    f""" 
    o produto do dobro do primeiro com a metade do segundo é {(inteiro*2) + ( numeroReal1/2)} \n
    a soma do triplo do primeiro com o terceiro é {(numeroReal1*3)+ numeroReal2} \n
    o terceiro elevado ao cabo é {numeroReal2 ** 3} \n
    """) 