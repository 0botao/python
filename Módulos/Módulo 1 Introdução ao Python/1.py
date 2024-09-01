# Módulo 1: Introdução ao Python

# 1.1 Instalação do Python e Configuração do Ambiente

# Antes de começarmos a programar em Python, precisamos instalar a linguagem no seu sistema e configurar um ambiente adequado para o desenvolvimento.

# 1.1.1 Como Instalar o Python

# 1. Windows:
# - Acesse o site oficial do Python: https://www.python.org/downloads/.
# - Baixe a versão mais recente estável do Python.
# - Durante a instalação, certifique-se de marcar a opção "Add Python to PATH". 
#   Isso permitirá que você execute Python diretamente do terminal.
# - Após a instalação, abra o Prompt de Comando e digite `python --version` para verificar se a instalação foi bem-sucedida.

# 2. MacOS:
# - O MacOS geralmente já vem com uma versão do Python instalada. No entanto, é recomendável instalar uma versão atualizada.
# - Use o Homebrew para instalar Python:
# ```bash
# brew install python
# ```
# - Após a instalação, verifique a versão instalada com `python3 --version`.

# 3. Linux:
# - A maioria das distribuições Linux já vem com Python pré-instalado.
# - Para instalar a versão mais recente:
# ```bash
# sudo apt-get update
# sudo apt-get install python3
# ```
# - Verifique a instalação com `python3 --version`.

# 1.1.2 Configuração de IDEs Populares

# Uma IDE (Integrated Development Environment) facilita a escrita, depuração e execução de códigos. Vamos configurar algumas IDEs populares para Python:

# 1. VS Code:
# - Baixe e instale o VS Code: https://code.visualstudio.com/.
# - Instale a extensão Python no VS Code:
#   - Abra o VS Code.
#   - Vá até o painel de extensões (ícone de quadrado na barra lateral esquerda).
#   - Pesquise por "Python" e instale a extensão oficial da Microsoft.
# - Configure o interpretador Python:
#   - Abra qualquer arquivo `.py`.
#   - Pressione `Ctrl + Shift + P` e digite "Python: Select Interpreter".
#   - Escolha a versão do Python instalada no seu sistema.

# 2. PyCharm:
# - Baixe e instale o PyCharm: https://www.jetbrains.com/pycharm/.
# - Durante a configuração inicial, o PyCharm detecta automaticamente a instalação do Python no seu sistema.
# - PyCharm é uma IDE poderosa com recursos específicos para Python, incluindo integração com virtual environments, testes, e ferramentas de depuração.

# 3. Jupyter Notebook (Opcional):
# - Para quem prefere um ambiente interativo, o Jupyter Notebook é uma ótima escolha, especialmente para data science e análise de dados.
# - Instale o Jupyter Notebook usando `pip`:
# ```bash
# pip install notebook
# ```
# - Inicie o Jupyter Notebook no terminal com:
# ```bash
# jupyter notebook
# ```
# - Um navegador será aberto, permitindo que você crie e execute blocos de código Python de maneira interativa.

# 1.1.3 Uso do Terminal e do Interpretador Python

# Após a instalação, é fundamental entender como usar o terminal e o interpretador Python:

# 1. Terminal:
# - O terminal (ou Prompt de Comando no Windows) é uma ferramenta poderosa para executar comandos, scripts e interagir com o sistema operacional.
# - Para abrir o terminal:
#   - Windows: Use o `Prompt de Comando` ou o `PowerShell`.
#   - MacOS/Linux: Use o `Terminal`.

# 2. Interpretador Python:
# - O interpretador Python permite que você execute comandos Python diretamente no terminal, ideal para testar pequenas porções de código.
# - Para iniciar o interpretador, digite `python` (ou `python3` em alguns sistemas) no terminal. Você verá algo como:
# ```plaintext
# Python 3.x.x (default, ...) 
# [GCC ...] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# ```
# - O prompt `>>>` indica que você está no ambiente interativo do Python. Aqui, você pode digitar expressões e ver os resultados instantaneamente.

# Exemplo: 
print("Hello, Python!")  # Este comando imprimirá "Hello, Python!" no terminal

# 1.2 Primeiros Passos com Python

# Com o Python instalado e o ambiente configurado, é hora de dar os primeiros passos na programação com Python.

# 1.2.1 O que é Python?

# Python é uma linguagem de programação de alto nível, criada por Guido van Rossum e lançada pela primeira vez em 1991. 
# Ela é conhecida por sua sintaxe clara e concisa, que facilita a leitura e a escrita de código.

# Python é:
# - Interpretada: O código Python é executado linha a linha, o que facilita o desenvolvimento e a depuração.
# - Multiparadigma: Python suporta múltiplos paradigmas de programação, incluindo programação procedural, orientada a objetos e funcional.
# - Altamente Versátil: Usada em desenvolvimento web, ciência de dados, automação, inteligência artificial, e muito mais.

# 1.2.2 Introdução ao Ambiente de Desenvolvimento

# Vamos criar nosso primeiro script Python.

# 1. Criando um Script:
# - Abra seu editor de texto ou IDE.
# - Crie um novo arquivo com a extensão `.py` (por exemplo, `hello.py`).
# - Escreva o seguinte código:

print("Hello, Python!")  # Este script imprime "Hello, Python!" no terminal

# 2. Salvando o arquivo.
# - Salve o arquivo com a extensão .py (exemplo: hello.py).

# 1.2.3 Executando Scripts Python

# Além de rodar scripts diretamente do terminal, você também pode executá-los dentro de sua IDE:

# 1. VS Code:
# - Abra o arquivo `.py` no VS Code.
# - Pressione `Ctrl + F5` para executar o código.
  
# 2. PyCharm:
# - Clique com o botão direito no arquivo `.py` e selecione "Run 'nome_do_arquivo.py'".

# 3. Jupyter Notebook:
# - Crie uma nova célula e digite:
print("Hello, Python!")  # Executa no Jupyter Notebook

# - Pressione `Shift + Enter` para executar a célula.

# Com isso, você já está pronto para começar a programar em Python! Este primeiro módulo cobre os conceitos básicos necessários para configurar seu ambiente de desenvolvimento e executar seus primeiros scripts.

# Se tiver alguma dúvida ou quiser revisar alguma parte, estou aqui para ajudar! Caso contrário, podemos prosseguir para o próximo módulo.
