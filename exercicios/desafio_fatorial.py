# Crie um código que calcula o fatorial de um número.
# O que é um fatorial de um número n?
# A multiplicação de n por todos os números anteriores a ela:

# 3! = 3 * 2 * 1
# 6! = 6 * 5 * 4 * 3 * 2 * 1


numero = int(input("Digite um núemro: "))
fatorial = 1
print(numero, "! = ", end="")
while numero > 0:
    print(numero, end='')
    print(" * " if numero > 1 else " = ", end='')
    fatorial *= numero
    numero -= 1
print(fatorial)
