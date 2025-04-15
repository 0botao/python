# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input(" digite um numero 1 "))
n2 = float(input(" digite um numero 2 "))
n3 = float(input(" digite um numero 3 ")) 

if n1 > n2 and n1 > n3: 
    print(f" é o maior  {n1}")
elif n2 > n1 and n2 > n3:
    print(f" é maior  {n2}")
elif n3 > n1 and n3 > n2: 
    print(f" é maior  {n3}")

else:
    print(" todos os numero sao iguais") 
if n1 < n2 and n1 < n3: 
    print(f" é menor  {n1}")
elif n2 < n1 and n2 < n3:
    print(f" é menor  {n2}")
elif n3 < n1 and n3 < n2: 
    print(f" é menor  {n3}")
else:
    print(" todos os numero sao iguais")