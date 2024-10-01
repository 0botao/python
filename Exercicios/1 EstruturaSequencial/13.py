# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input(' digite a sua altura'))
sexo = input(' Digite "f" para sexo feminino e "m" para sexo masculino')

if sexo == "f":
    feminino = (62.1 * altura) - 44.7
    print(f' o seu peso idela é de {feminino}') 
elif sexo == "m":
    masculino = (72.7 * altura) - 58
    print(f' o seu peso idela é de {masculino}')
else:
    print("entrada invalida")
