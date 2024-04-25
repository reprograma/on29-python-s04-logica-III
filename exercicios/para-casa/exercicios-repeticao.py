# Desenvolva um programa que faça uma tabuada de um número qualquer inteiro que será digitado pelo usuário, mas
# a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
# pelo usuário, conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:

# 5 x 4: 20
# 5 x 5: 25
# 5 x 6: 30
# 5 x 7: 35

# Observação: Você deve verificar se o usuário não digitou o final menor que o inicial.

tabuada = int(input("Qual tabuada de multiplicação você deseja fazer? "))
início = int(input("Por qual número você deseja iniciar sua tabuada? "))
fim = int(input("E por qual número você quer que a tabuada acabe? "))


for item in range(tabuada, fim + 1):
    print(f"{tabuada} X {item} = {tabuada * item}")

print("Fim do programa!")