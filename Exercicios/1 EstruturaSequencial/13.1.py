while True:
    try:
        altura = float(input('Digite a sua altura: '))
        if altura <= 0:
            raise ValueError("A altura deve ser um número positivo.")
        break
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira um valor válido para altura.")

while True:
    sexo = input('Digite "f" para sexo feminino e "m" para sexo masculino: ').lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Entrada inválida. Por favor, digite 'f' para feminino ou 'm' para masculino.")

if sexo == "f":
    feminino = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é de {feminino:.2f} kg.')
elif sexo == "m":
    masculino = (72.7 * altura) - 58
    print(f'O seu peso ideal é de {masculino:.2f} kg.')
