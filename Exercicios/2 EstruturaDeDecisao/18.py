#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 




def verificador(a):
    a = a.strip()

    if a == '':
        print(' na pode deixar o espaço em branco \n')
        return None
    try:
        a = float(a)
        if 1 <= a <= 999:
            return f'{(a // 100):.0f} centena(s) , {(a // 10):.0f} dezena(s) e {((a % 100) % 10):.0f} unidade(s)'
    except ValueError:
        print('eroo de caracteres ')
        return None
while True:
    numero = input(' digite umnumero de 1 até 999 \n ')
    print(verificador(numero))











