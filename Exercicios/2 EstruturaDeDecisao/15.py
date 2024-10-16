# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# # Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes; 

def verificadorVazio(a):
    while True:
        a = a.strip()

        if a == "":
            print(' nao pode deixar o espaço em branco ')
            return None
        try:
            a = float(a)
            return a 
        except ValueError:
            print('erro de caracteres ')
            return None
    
def tipoTriangulo(a, b, c):
    # Verifica se os lados formam um triângulo
    if a + b > c and a + c > b and b + c > a:
        print('Os valores formam um triângulo válido.')
        
        # Verifica o tipo de triângulo
        if a == b == c:
            print('Este é um triângulo equilátero.')
        elif a == b or b == c or a == c:
            print('Este é um triângulo isósceles.')
        else:
            print('Este é um triângulo escaleno.')
    else:
        print('Os valores não formam um triângulo válido.')
while True:
    while True:
        n1 = input('digite o pimeiro lado \n')
        n1 = verificadorVazio(n1)
        if n1 is not None:
            break
    while True:
        n2 = input(' digite o segundo lado \n')
        n2 = verificadorVazio(n2)
        if n2 is not None:
            break
    while True:
        n3 = input('digite o terceiro lado \n')
        n3 = verificadorVazio(n3)
        if n3 is not None:
            break
    tipoTriangulo(n1,n2,n3)


