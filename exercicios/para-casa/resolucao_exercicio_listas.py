lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(20):
  numero = int(input("Insira um número: "))
  lista_numeros.append(numero)
  if numero%2 == 0:
    lista_pares.append(numero)
  else:
    lista_impares.append(numero)

print(f"A lista de números gerada é: {lista_numeros}.")
print(f"Os pares são {lista_pares}, e os ímpares são {lista_impares}.")