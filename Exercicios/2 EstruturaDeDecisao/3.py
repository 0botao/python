# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido 

while True:
    try:
        sexo = input(" digite M para masculino e F para feminino ").strip()

        if sexo == "":
            print(" digite uma vogal valida  ") 
            continue 

        try:
            if sexo == "F":
                print(" a pessoa é do sexo femininoo ")
            elif sexo == "M":
                print(" a pesoa é do sexo masculino")
        except ValueError:
            print(" digite um caractere valido ")
    except ValueError:
        print(" digite uma vogal valida ")