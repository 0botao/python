# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e
# apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez. 

while True:
    while True: 
        try:
            nota1 = float(input(' digite a sua primeira nota ')) 
            if nota1 > 10 and nota1 < 0:
                print(' nota1 invalida')
                continue
            else:
                print('nota1 valida')
                break
        except ValueError:
            print(' digite apenas numeros  ')


    while True: 
        try:
            nota2 = float(input(' digite a sua segunda nota ')) 
            if nota2 > 10 and nota1 < 0:
                print(' nota2 invalida')
                continue
            else:
                print('nota2 valida')
                break
        except ValueError:
            print(' digite apenas numeros  ')
    
    if  ((nota1 + nota2)/2) == 10:
        print('aprovado com distinção') 
    elif ((nota1 + nota2)/2) < 7:
        print('reprovado') 
    elif ((nota1 + nota2)/2) >=7:
        print('aprovado ')
