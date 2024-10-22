# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno 
# e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#| A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10 


def verificadorVazio(a):
    a = a.strip()

    if a == '':
        print(' Nao se pode deixar o espaço em  branco ')
        return None
    try:
        a = float(a)

    except ValueError:
        print(' erro de caracteres ')
        return None 
    
def media(a):
    print()

while True:
    lista = []
    
    for i in range(4):
        nota = None
        
        while nota is None:
            entrada = input(f' digite a sua {(i + 1)}º nota ')
            nota = verificadorVazio(entrada)
        lista.append(nota) 