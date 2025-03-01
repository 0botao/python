"""Enunciado: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre:

O salário bruto.

Quanto foi pago ao INSS (8% do salário bruto).

Quanto foi pago ao sindicato (5% do salário bruto).

O salário líquido (descontando 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato).""" 

hora = float(input(" o quanto voce ganha por hora ? \n"))
horasTrabalhadasdas  = float(input(" quantas horas trabalhadas ? \n "))

print(
f"""
Sálario total   :     {hora*horasTrabalhadasdas}
Inss            :     {(hora*horasTrabalhadasdas) * 0.08}
Sindicato       :     {(hora*horasTrabalhadasdas) * 0.05}
Ir              :     {(hora*horasTrabalhadasdas) * 0.11}
Sálario Líquido :     {(hora*horasTrabalhadasdas) - ((hora*horasTrabalhadasdas) * 0.24)}

"""
)