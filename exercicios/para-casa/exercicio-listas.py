# Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e
# os números ÍMPARES no vetor ímpar. Imprima os três vetores.


programa = [[], [], []]
valor = 0

for item in range(1,21):
    valor = int(input(f"Digite o {item}o. número inteiro: "))
    programa[0].append(valor)
    if valor % 2 == 0:
        programa[1].append(valor)
    else:
        programa[2].append(valor)

print('-=' * 30)

print(f"Todos os números inteiros: {programa[0]}")
print(f"Todos os números pares: {programa[1]}")
print(f"Todos os números ímpares: {programa[2]}")

print("Fim do programa!")