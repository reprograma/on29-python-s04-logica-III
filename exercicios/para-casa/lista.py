inteiros = []
pares = []
impares = []
print('Lista de 20 números inteiros')
for item in range(0, 20):
    numero = int(input('Digite o número escolhido: '))
    inteiros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('Os números digitados foram: {}.'.format(inteiros))
print('Os números pares são {} e os números ímpares são {}.'.format(pares, impares))

