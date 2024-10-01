# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#  Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a 
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
#  na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 

while True:
    try:
        peso = float(input(' digite a qauntidade de peso pescado pelo joâo \n'))
        if peso > 50:
            print(f' joao vai pagar cerca de {(peso - 50) * 4} \n')
            break
        else:
            print(' joao nao vai pagar nada \n')
            break
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira um valor válido para altura. \n")