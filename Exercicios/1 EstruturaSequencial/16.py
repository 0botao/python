''''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.''' 


while True:
    try:
        metros = float(input(' digite a quantida de metros a ser  pintada \n ')) 
        area = metros * 3 

        if area <= 0: 
            print(' quantidade invalida ')
        elif area  <= 18:
            print(' voce so precisa de uma lata de tinta, que sai no valor de R$80,00')
        elif area > 18:
            aproximando = area / 18 
            if aproximando > int(aproximando):
                aproximando = int(aproximando) + 1
                print(f'o numero de latas que voce precisa é de {aproximando} que sai no valor de {aproximando * 80} ')
            else:
                print()
        else:
            print()

    except ValueError as e:
        print(f' erro , o caractere {e} é invalido ') 