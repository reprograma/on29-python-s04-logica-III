# vetor = lista
lista = []
lista_par = []
lista_impar = []

for item in range(21):
    lista.append(item)
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)

print(lista)
print(lista_par)
print(lista_impar)
