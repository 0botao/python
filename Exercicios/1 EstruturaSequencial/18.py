'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
''' 

while True:
    while True:
        mb = input(" qual o tamanho do arquivo em MB ? \n").strip()
        if mb == '':
            print(' erro no valor digitado ')
            continue

        try:
            mb = float(mb)
            if mb <=0:
                print("O número deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("entrada invalida ")
                
    while True:
        velocidade = input(" qual a velocidade da sua internet ? \n").strip()
        if velocidade == '':
            print(' erro no valor digitado ')
            continue
        try:
            velocidade = float(velocidade)
            if velocidade <=0:
                print("a velocidade da internet tem que ser maior que zero .")
                continue  
            break

        except ValueError:
            print("entrada invalida ")

    print(f' o tempo aproximado de dowload é de cerca de {(mb / velocidade):.2f} segundo ')
        