#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

x = []
pares = []
impares = []

for i in range(1, 21):
    x.append(i)
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Lista com todos números:", x)
print("Lista com os números pares:", pares)
print("Lista de números ímpares:", impares)
print("Fim do programa")