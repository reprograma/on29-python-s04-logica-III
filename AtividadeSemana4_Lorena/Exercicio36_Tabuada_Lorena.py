base_tabuada = int(input("\nInsira um número para obter a tabuada deste número: "))
inicio_tabuada = int(input("Insira um número inicial para a tabuada: "))
fim_tabuada = int(input("Insira um número final para a tabuada: ")) + 1

if inicio_tabuada <= fim_tabuada:
    for fator in range(inicio_tabuada, fim_tabuada):
        produto = base_tabuada * fator
        print(F"{base_tabuada} x {fator} = {produto}")
else: 
    print("\nO número inicial da tabuada precisa ser inferior ao número final.") 