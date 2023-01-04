nomes = []
cpf = []
quant_quartos = 0
while True:
    quarto = input(f"deseja um quarto?(s/n) ")
    if quarto == "s":
        quant_quartos += 1
    elif quarto == "n":
        print("nenhum quarto escolhido.")
        break    

    quant_pessoas = int(input("quantas pessoas serão hospedadas no quarto? "))

    for x in range(quant_pessoas):
        nomes.append(input(f"nome da pessoa {x+1}: "))
        for i in range(1):
            cpf.append(input(f"CPF de {nomes [x]}: "))
            print("")

    for x in range(1):
        print("==============================================")
        print(f"QUARTO {quant_quartos}")
        print(f"numero de hóspedes: {quant_pessoas}")
        print("______")

        for x in range(quant_pessoas):
            print(f"nome: {nomes[x]}")
            print(f"CPF: {cpf[x]}")
            print("--------------------")
