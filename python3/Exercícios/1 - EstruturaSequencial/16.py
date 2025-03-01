"""Questão 16:
Enunciado: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de 
Internet (em Mbps). Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
""" 

tamanhoMb = float(input(" Digite o tamanho do arquivo : \n "))
velocidadeInternet  = float(input(" digite a velocidade da sua internet : \n"))

print(
f"""
O tempo aprocimado em minutos para baixar esse arquivo {(tamanhoMb/velocidadeInternet):.0f} minutos 
"""
)