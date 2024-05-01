# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.



# Lista para armazenar os números inteiros
numeros = []

# Vetores para armazenar os números pares e ímpares
pares = []
impares = []

# Adicionando números pares e ímpares à lista e às listas pares e ímpares
for item in range(21):
    numeros.append(item)  # Adiciona todos os números à lista 'numeros'
    if item % 2 == 0:
        pares.append(item)  # Adiciona número par à lista 'pares'
    else:
        impares.append(item)  # Adiciona número ímpar à lista 'impares'

print("numeros", numeros)
print("pares", pares)
print("impares", impares)
