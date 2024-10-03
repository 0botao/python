# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

while True:
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    try:
        letra = input('digite a letra que voce queira sabe se é vogal ou consoante ? \n ')

        if len(letra) > 1:
            print(' por favor insira so um carectere ')
            continue
        else:
            if letra in vogais: 
                print(' é uma vogal ')
            else:
                print(' é uma consoante') 
                
    except ValueError:
        print(' o que voce digitou é um numero entao nao vale ')
