

lista = []
lista_par = []
lista_impar = []
num1 = input("Digite um número: ")
num2 = int(num1) + 20
print("O ultimo número será: " + str(num2))
#Segue então a sequência das três listas.
for item in range(int(num1), int(num2), 1):
    lista.append(item)

for item in range(int(num1), int(num2), 1):
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)


print("Sequência de números inteiros: " + str(lista))
print("Sequência de números pares: " + str(lista_par))
print("Sequência de números impares: " + str(lista_impar))
