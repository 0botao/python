# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input(f" Digite a sua altura : \n"))

print(f"""
      O seu peso ideal para homens é  {((72.7 * altura) - 58):.2f} Kg \n
      O seu peso ideal para mulheres é {((62.1 * altura) - 44.7):.2f}
       """)