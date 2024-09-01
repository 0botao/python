# Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

media = []
for i in range(4):
    n1 = float(input(f" digite a sua {i + 1} "))
    media.append(n1)

soma = 0

for i in media:
    soma += i 

print(f"a media final foi de  {soma /4 }")
