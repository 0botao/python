# Vamos reformular para garantir que tudo esteja alinhado com o formato correto. Vou converter as explicações em comentários e 
# manter apenas o código Python como executável, seguindo o padrão do que foi feito anteriormente.



### **Módulo 2: Sintaxe e Conceitos Básicos**

#### **2.1 Sintaxe Básica**


# Python é conhecido por sua sintaxe simples e clara. Vamos explorar os elementos básicos que compõem a sintaxe da linguagem.

# 2.1.1 Variáveis e Tipos de Dados
# Em Python, você pode criar variáveis simplesmente atribuindo valores a elas. 
# Não é necessário declarar o tipo da variável explicitamente.

# Exemplos de variáveis com diferentes tipos de dados:
numero_inteiro = 10  # Inteiro
numero_decimal = 3.14  # Ponto flutuante (float)
texto = "Olá, Mundo!"  # String
booleano = True  # Booleano (True ou False)

# Python é uma linguagem de tipagem dinâmica, o que significa que o tipo da variável 
# é determinado automaticamente com base no valor atribuído.

# 2.1.2 Operadores Básicos
# Python suporta uma variedade de operadores, incluindo operadores aritméticos, de comparação e lógicos.

# Exemplos de operadores aritméticos:
soma = 5 + 3  # Adição
subtracao = 10 - 2  # Subtração
multiplicacao = 4 * 3  # Multiplicação
divisao = 8 / 2  # Divisão (resultado será float)
divisao_inteira = 8 // 3  # Divisão inteira
modulo = 10 % 3  # Módulo (resto da divisão)
exponenciacao = 2 ** 3  # Exponenciação (2 elevado à potência 3)

# Exemplos de operadores de comparação:
igual = (5 == 5)  # Igualdade
diferente = (5 != 3)  # Diferença
maior_que = (7 > 3)  # Maior que
menor_que = (4 < 10)  # Menor que
maior_ou_igual = (5 >= 5)  # Maior ou igual
menor_ou_igual = (3 <= 4)  # Menor ou igual

# Exemplos de operadores lógicos:
e_logico = (True and False)  # E lógico (ambos precisam ser True)
ou_logico = (True or False)  # OU lógico (pelo menos um precisa ser True)
nao_logico = not True  # Negação lógica (inverte o valor booleano)

# 2.1.3 Comentários e Boas Práticas
# Comentários são usados para explicar o código e são ignorados pelo interpretador.
# Eles são essenciais para tornar o código mais legível e compreensível.

# Exemplos de comentários:
# Este é um comentário de linha única.

"""
Este é um comentário de múltiplas linhas.
Também pode ser usado para documentar funções ou scripts inteiros.
"""

# Boas práticas:
# - Use nomes de variáveis descritivos para facilitar o entendimento do código.
# - Utilize comentários para explicar trechos de código complexos.
# - Siga convenções de estilo como o PEP 8 para manter um código limpo e organizado.


#### **2.2 Controle de Fluxo**


# 2.2.1 Condicionais (if, elif, else)
# As estruturas condicionais permitem que você execute blocos de código com base em certas condições.

# Exemplo de estrutura condicional:
idade = 18

if idade >= 18:
    print("Você é maior de idade.")  # Executa este bloco se a condição for verdadeira
elif idade >= 16:
    print("Você é quase maior de idade.")  # Executa se a primeira condição for falsa e esta for verdadeira
else:
    print("Você é menor de idade.")  # Executa se todas as condições anteriores forem falsas

# 2.2.2 Estruturas de Repetição (for, while)
# Estruturas de repetição permitem que você execute um bloco de código várias vezes.

# Exemplo de loop 'for':
for i in range(5):
    print(f"Iteração {i}")  # Executa o bloco de código 5 vezes, com i variando de 0 a 4

# Exemplo de loop 'while':
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o contador até que a condição seja falsa

# 2.2.3 Controle de Loop (break, continue, pass)
# 'break' interrompe o loop, 'continue' pula para a próxima iteração, e 'pass' não faz nada (útil como placeholder).

# Exemplo de uso do 'break':
for i in range(10):
    if i == 5:
        break  # Interrompe o loop quando i é igual a 5
    print(i)

# Exemplo de uso do 'continue':
for i in range(10):
    if i % 2 == 0:
        continue  # Pula para a próxima iteração se i for par
    print(i)

# Exemplo de uso do 'pass':
for i in range(10):
    if i % 2 == 0:
        pass  # Placeholder, não faz nada
    else:
        print(i)


# Esse módulo cobre os conceitos básicos de sintaxe e controle de fluxo em Python, proporcionando uma base sólida para avançar no
#  aprendizado da linguagem. As explicações estão em comentários, e o código executável é separado para que você possa rodar e 
# testar os exemplos diretamente.

# Se precisar de mais alguma coisa ou quiser prosseguir para o próximo módulo, estou aqui para ajudar!