# Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números impares no vetor IMPAR. Imprima os 3 vetores.

numeros = input("Insira 20 números inteiros separados por espaço: ").split()

numeros_inteiros = []

par = []

impar = []

for numero in numeros:
    numeros_inteiros.append(int(numero))
    if int(numero) % 2 == 0:
        par.append(int(numero))
    else:
        impar.append(int(numero))

print(f"\nNúmeros inseridos: {numeros_inteiros}")
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")