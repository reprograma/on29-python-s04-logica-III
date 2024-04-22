'''
Desenvolva um programa que faça a tabuada de um número inteiro que será digitado pelo usuário, mas a tabuada não deve necessáriamente iniciar em 1 e terminar em 10, os valores inicial e final devem ser informados também pelo usuário, conforme o exemplo abaixo:

Montar a tabuada de : 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35

Observação: Você deve verificar se o usuário não digitou o valor final menor que o inicial.
'''

def tabuada(numero, inicio, fim):
    if fim < inicio:
        print("\nErro: O valor final não pode ser menor que o valor inicial.")
        return
    
    print(f"\nVou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

tabuada(numero, inicio, fim)