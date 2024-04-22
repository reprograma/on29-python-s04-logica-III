tabuada = int(input("Digite o número da tabuada: "))
comeca = int(input("Digite o número de início da tabuada: "))
fim = int(input("Digite o número de fim da tabuada: "))

if comeca > fim:
    print("A variável de começo não pode ser maior que a de fim.")
else:
    for numero in range(comeca, fim, 1):
        print(f"tabuada do {tabuada}, {numero} * {tabuada} = {numero*tabuada}")