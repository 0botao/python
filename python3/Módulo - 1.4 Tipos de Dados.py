# Números inteiros (int)
# Inteiros representam números inteiros, positivos ou negativos, sem ponto decimal.
numero_inteiro = 10
print(type(numero_inteiro))  # <class 'int'>

# Números de ponto flutuante (float)
# Números de ponto flutuante representam números com ponto decimal.
numero_flutuante = 10.5
print(type(numero_flutuante))  # <class 'float'>

# Strings (str)
# Strings são sequências de caracteres, delimitadas por aspas simples ou duplas.
mensagem = "Olá, mundo!"
print(type(mensagem))  # <class 'str'>

# Listas (list)
# Listas são estruturas que armazenam uma sequência ordenada de elementos, podendo incluir diferentes tipos de dados.
lista = [1, 2, 3, 4, 5]
print(type(lista))  # <class 'list'>

# Tuplas (tuple)
# Tuplas são semelhantes às listas, mas são imutáveis (não podem ser modificadas após a criação).
tupla = (1, 2, 3, 4, 5)
print(type(tupla))  # <class 'tuple'>

# Dicionários (dict)
# Dicionários são coleções de pares chave-valor, onde cada chave é única.
dicionario = {"chave1": "valor1", "chave2": "valor2"}
print(type(dicionario))  # <class 'dict'>

# Conjuntos (set)
# Conjuntos são coleções desordenadas de elementos únicos.
conjunto = {1, 2, 3, 4, 5}
print(type(conjunto))  # <class 'set'>

# Conjuntos Imutáveis (frozenset)
# Conjuntos imutáveis são semelhantes aos conjuntos (set), mas não podem ser modificados após a criação.
frozenset_exemplo = frozenset([1, 2, 3, 4, 5])
print(type(frozenset_exemplo))  # <class 'frozenset'>
