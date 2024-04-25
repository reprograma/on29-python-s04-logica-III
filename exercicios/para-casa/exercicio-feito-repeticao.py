print("Vamos montar uma tabuada?")

inicio = int(input("Montar tabuada de: "))
meio = int(input("Começar pelo dígito: "))
fim = int(input("Terminar em: "))

def tabuada_calculo(inicio, meio, fim):
    fim = fim + 1
    print("Vou montar a tabuada de ", str(inicio), "começando em ", str(meio), "e terminando em ", str(fim))
    for item in range(meio, fim):
        print(inicio * item)

tabuada_calculo(inicio, meio, fim)