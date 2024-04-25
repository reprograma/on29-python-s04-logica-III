#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

print("Vamos montar uma tabuada?")

inicio = int(input("Montar tabuada de: "))
meio = int(input("Começar pelo dígito: "))
fim = int(input("Terminar em: "))



def tabuada_calculo(inicio, meio, fim):
    print("Vou montar a tabuada de" + str(inicio) + "começando em " + str(meio) + "e terminando em " + str(fim))
    fim = fim + 1

    for numero in range(meio, fim):
        print ( "O resultado é: " + str(inicio) * str(numero))
        

tabuada_calculo(inicio, meio, fim)