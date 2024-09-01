# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o 
# total do seu salário no referido mês. 

ganhaHoras= float(input(" quanto voce ganhar por hora ? ")) 
dias = float(input(" dias trabalhados ")) 

print(f"Ao final do mês voce vai ganhar cerca de {(ganhaHoras*dias):.0f }") 