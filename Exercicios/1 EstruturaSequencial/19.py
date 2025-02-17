import tkinter as tk  # Importa o módulo tkinter

# Função para atualizar a mensagem
def atualizar_mensagem():
    label.config(text="Olá, você clicou no botão!")

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Interface")  # Define o título da janela
janela.geometry("300x200")  # Define o tamanho da janela (largura x altura)

# Cria uma label (texto) na janela
label = tk.Label(janela, text="Bem-vindo à interface!", font=("Arial", 14))
label.pack(pady=20)  # Adiciona a label à janela com espaço vertical

# Cria um botão na janela
botao = tk.Button(janela, text="Clique Aqui", command=atualizar_mensagem, font=("Arial", 12))
botao.pack(pady=10)  # Adiciona o botão à janela com espaço vertical

# Inicia o loop principal da janela (mantém a janela aberta)
janela.mainloop()