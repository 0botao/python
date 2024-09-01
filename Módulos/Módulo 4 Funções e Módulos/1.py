# Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
# Elas permitem modularizar seu código, tornando-o mais organizado e fácil de manter.

# 4.1.1 Sintaxe de Funções em Python
# Em Python, as funções são definidas usando a palavra-chave `def`, seguida do nome da função e dos parênteses ().

# Exemplo de uma função simples:
def saudacao():
    print("Olá, Mundo!")

# Para chamar a função, basta usar o nome dela seguido de parênteses:
saudacao()  # Isso imprimirá "Olá, Mundo!" no terminal

# 4.1.2 Parâmetros e Argumentos
# As funções podem receber parâmetros, que são valores passados para a função para personalizar seu comportamento.

# Exemplo de função com parâmetros:
def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")

# Chamando a função com um argumento:
saudacao_personalizada("João")  # Isso imprimirá "Olá, João!" no terminal

# 4.1.3 Funções com Valores de Retorno
# Algumas funções retornam um valor usando a palavra-chave `return`.

# Exemplo de função com valor de retorno:
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado:
resultado = soma(5, 3)  # Resultado será 8

# Funções podem retornar múltiplos valores como uma tupla:
def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

# Chamando a função e desempacotando os valores:
soma_resultado, diferenca_resultado = operacoes(10, 5)

# Python vem com várias funções integradas que você pode usar sem precisar defini-las.
# Elas são muito úteis para realizar operações comuns.

# Exemplos de funções integradas:
tamanho = len("Olá, Mundo!")  # Retorna o tamanho da string (12)
maior_numero = max(1, 2, 3, 4, 5)  # Retorna o maior número (5)
menor_numero = min(1, 2, 3, 4, 5)  # Retorna o menor número (1)
soma_total = sum([1, 2, 3, 4, 5])  # Retorna a soma de todos os elementos (15)

# A função `type` retorna o tipo de dado de uma variável:
tipo = type(10)  # Retorna <class 'int'>

# Módulos são arquivos que contêm código Python (funções, variáveis, etc.) e que podem ser importados e reutilizados em outros scripts.
# Pacotes são coleções de módulos organizados em diretórios.

# 4.3.1 Importando Módulos
# Para usar um módulo, você precisa importá-lo usando a palavra-chave `import`.

# Exemplo de importação de um módulo:
import math  # Módulo de funções matemáticas

# Agora podemos usar as funções do módulo `math`:
raiz_quadrada = math.sqrt(16)  # Retorna a raiz quadrada de 16 (4.0)
pi = math.pi  # Acessa o valor de pi (3.141592653589793)

# Também é possível importar apenas partes específicas de um módulo:
from math import sqrt, pi

# Agora podemos usar `sqrt` e `pi` diretamente:
raiz_quadrada = sqrt(25)  # Retorna 5.0

# 4.3.2 Instalando Pacotes com `pip`
# Python possui um gerenciador de pacotes chamado `pip`, que permite instalar e gerenciar pacotes de terceiros.

# Para instalar um pacote, use o comando `pip install nome_do_pacote` no terminal.

# Exemplo de instalação do pacote `requests` para fazer requisições HTTP:
# pip install requests

# Após a instalação, você pode importar e usar o pacote em seu código:
import requests

# Exemplo de uso do pacote `requests`:
resposta = requests.get("https://api.github.com")
status_code = resposta.status_code  # Retorna o código de status da resposta (200 para sucesso)

# 4.3.3 Introdução ao PyPI (Python Package Index)
# PyPI é o repositório oficial de pacotes Python. É onde você pode encontrar e publicar pacotes.

# Você pode navegar pelos pacotes disponíveis em https://pypi.org/
# Para instalar um pacote do PyPI, basta usar `pip install nome_do_pacote` como mostrado anteriormente.

