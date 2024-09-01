# Listas são coleções ordenadas de elementos que podem ser de diferentes tipos. 
# As listas em Python são mutáveis, o que significa que podemos alterar seus elementos após a criação.

# 3.1.1 Criando e Manipulando Listas
# Para criar uma lista, basta colocar os elementos entre colchetes [].

# Exemplo de criação de listas:
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
mista = [1, "texto", 3.14, True]

# Podemos acessar os elementos de uma lista usando índices (começando do 0):
primeiro_numero = numeros[0]  # Acessa o primeiro elemento (1)
segunda_fruta = frutas[1]  # Acessa o segundo elemento ("banana")

# 3.1.2 Métodos de Lista
# Python oferece vários métodos para manipular listas.

# Adicionar elementos:
numeros.append(6)  # Adiciona o número 6 ao final da lista

# Remover elementos:
frutas.remove("banana")  # Remove a primeira ocorrência de "banana"

# Ordenar a lista:
numeros.sort()  # Ordena a lista de números em ordem crescente

# Obter o tamanho da lista:
tamanho = len(mista)  # Retorna o número de elementos na lista

# Listas são mutáveis, então você pode alterar diretamente seus elementos:
numeros[0] = 10  # Altera o primeiro elemento para 10

# Tuplas são semelhantes às listas, mas são imutáveis, o que significa que seus elementos não podem ser alterados após a criação.
# Tuplas são úteis para armazenar dados que não devem ser modificados.

# 3.2.1 Criando e Acessando Tuplas
# Para criar uma tupla, use parênteses ().

# Exemplo de criação de tupla:
coordenadas = (10.0, 20.0)
valores_mistos = (1, "texto", 3.14, False)

# Acessando elementos de uma tupla (similar a listas):
x = coordenadas[0]  # Acessa o primeiro elemento (10.0)

# 3.2.2 Operações com Tuplas
# Embora as tuplas sejam imutáveis, podemos realizar algumas operações úteis.

# Concatenar tuplas:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2  # Resultado: (1, 2, 3, 4, 5, 6)

# Desempacotamento de tuplas:
a, b, c = tupla1  # a=1, b=2, c=3

# Verificar se um elemento está na tupla:
existe = 2 in tupla1  # Resultado: True
# Dicionários são coleções não ordenadas de pares chave-valor.
# Eles permitem associar uma chave única a um valor.

# 3.3.1 Criando e Acessando Dicionários
# Para criar um dicionário, use chaves {} com pares chave: valor.

# Exemplo de criação de dicionário:
dados_pessoais = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Acessando valores a partir de chaves:
nome = dados_pessoais["nome"]  # Acessa o valor associado à chave "nome" ("João")

# 3.3.2 Métodos de Dicionários
# Dicionários em Python têm métodos úteis para manipulação de dados.

# Adicionar um novo par chave-valor:
dados_pessoais["profissao"] = "Engenheiro"

# Remover um par chave-valor:
idade = dados_pessoais.pop("idade")  # Remove a chave "idade" e retorna o valor (30)

# Verificar se uma chave existe no dicionário:
existe_cidade = "cidade" in dados_pessoais  # Resultado: True

# Obter todas as chaves ou valores:
chaves = dados_pessoais.keys()  # Retorna todas as chaves do dicionário
valores = dados_pessoais.values()  # Retorna todos os valores do dicionário

# Conjuntos são coleções não ordenadas de elementos únicos.
# Eles são úteis quando você precisa garantir que os elementos não se repitam.

# 3.4.1 Criando e Manipulando Conjuntos
# Para criar um conjunto, use chaves {} ou a função set().

# Exemplo de criação de conjunto:
numeros = {1, 2, 3, 4, 5}
letras = set("abacaxi")  # Resultado: {'a', 'b', 'c', 'x', 'i'}

# Adicionar elementos:
numeros.add(6)  # Adiciona o elemento 6 ao conjunto

# Remover elementos:
numeros.remove(3)  # Remove o elemento 3 do conjunto

# 3.4.2 Operações com Conjuntos
# Conjuntos suportam operações matemáticas como união, interseção e diferença.

# União de conjuntos:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1 | conjunto2  # Resultado: {1, 2, 3, 4, 5}

# Interseção de conjuntos:
intersecao = conjunto1 & conjunto2  # Resultado: {3}

# Diferença de conjuntos:
diferenca = conjunto1 - conjunto2  # Resultado: {1, 2}

# Verificar se um elemento está no conjunto:
existe = 4 in conjunto2  # Resultado: True


# Em Python, a função `input()` é usada para capturar dados fornecidos pelo usuário através do teclado.
# Por padrão, o que o usuário digita é tratado como uma string (texto).

# Exemplo básico de entrada de dados:
nome = input("Qual é o seu nome? ")  # O programa espera até que o usuário digite algo e pressione Enter
print(f"Olá, {nome}!")  # Exibe uma mensagem personalizada

# Capturando e convertendo tipos de dados:
idade = input("Quantos anos você tem? ")  # Captura a idade como uma string
idade = int(idade)  # Converte a string capturada em um número inteiro

# Verificando se a conversão foi bem-sucedida:
print(f"Você tem {idade} anos.")

# A função `print()` é usada para exibir informações na tela.
# Ela pode receber múltiplos argumentos, que serão convertidos para string e concatenados com um espaço.

# Exemplo básico de saída de dados:
print("Olá, mundo!")

# Saída com variáveis:
nome = "João"
idade = 30
print("Nome:", nome, "| Idade:", idade)

# Saída formatada:
print(f"Nome: {nome} | Idade: {idade}")  # Usa f-strings para formatar a saída de forma mais elegante

# Python oferece várias maneiras de formatar strings para exibir dados de maneira clara e legível.

# Usando a função `format()`:
mensagem = "Olá, {}. Você tem {} anos.".format(nome, idade)
print(mensagem)

# Usando f-strings (Python 3.6+):
print(f"Olá, {nome}. Você tem {idade} anos.")

# Especificando a quantidade de casas decimais em números:
pi = 3.14159
print(f"O valor de pi com duas casas decimais: {pi:.2f}")  # Exibe o número com 2 casas decimais

# Embora o foco aqui seja a entrada e saída de dados através do terminal, 
# é importante mencionar que Python também facilita a leitura e escrita de arquivos.

# Abrindo um arquivo para escrita:
with open("saida.txt", "w") as arquivo:
    arquivo.write("Esta é uma linha de texto.\n")

# Lendo um arquivo:
with open("saida.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)  # Exibe o conteúdo do arquivo
