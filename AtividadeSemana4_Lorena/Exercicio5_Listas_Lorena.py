lista_numeros = []
lista_numeros_pares = []
lista_numeros_impares = []

print("\nLista de números inteiros de 1 a 20:")

for lista_completa in range(0, 21, 1):
    lista_numeros.append(lista_completa)

for lista_pares in range (0, 21, 2):
    lista_numeros_pares.append(lista_pares)

for lista_impares in range (1,  21, 2):
    lista_numeros_impares.append(lista_impares)


print(f"\nLista completa: {lista_numeros}")
print(f"\nLista de números pares: {lista_numeros_pares}")
print(f"\nLista números ímpares: {lista_numeros_impares}")