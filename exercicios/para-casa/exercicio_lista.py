interacao = 1
numero = 0
lista = []
par = []
impar = []

while interacao <= 20:
    numero = int(input(f"Digite o {interacao}º número: "))
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    interacao += 1

print(f"lista total: {lista}")
print(f"lista par: {par}")
print(f"lista impar: {impar}")
