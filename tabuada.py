# Desenvolva um programa que faça a tabuada de um número
# qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 
# 1 e terminar em 10, o valor inicial e final devem ser
# informados também pelo usuário, conforme exemplo abaixo:

#     Montar a tabuada de: 5
#     Começar por: 4
#     Terminar em: 7

#     Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#     5 X 4 = 20
#     5 X 5 = 25
#     5 X 6 = 30
#     5 X 7 = 35

# solicita o usuario o a tabuada, valor inicial e final da operaçao

tabuada = int(input("Digite a tabuada que você deseja:"))

valor_inicial = int(input("Digite o valor incial:"))

valor_final = int(input("Digite o valor final:"))

print("gostaria de multiplicar a tabuada de",tabuada,"com inicio em",valor_inicial,"e fim em", valor_final)

#fazendo um laço de repetição
for i in range(valor_inicial, valor_final + 1):
    resultado = tabuada * i
    print(f"{tabuada} X {i} = {resultado}")