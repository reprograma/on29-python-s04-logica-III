# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
# o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

tabuada = int(input("Digite o número da tabuada que deseja: "))
comeco = int(input("Digite o número inicial da tabuada desejada: "))
fim = int(input("Digite o número final da tabuada desejada: "))

while comeco < fim+1:
    print(comeco, " X ", tabuada, " = ", comeco * tabuada)
    comeco = comeco + 1
