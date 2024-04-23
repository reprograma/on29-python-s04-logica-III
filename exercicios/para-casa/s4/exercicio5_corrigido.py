
#Pra não retornar lista vazia caso usuário coloque o 'stop' menor que o 'start'
while True:
    start = int(input("Digite um valor inicial: "))
    stop = int(input("Digite um valor final: "))
    if start <= stop:
        break
    else:
        print("O valor inicial deve ser menor ou igual ao valor final. Por favor, tente novamente.")

intervalo = list(range(start, stop+1))
pares = []
impares = []

for i in intervalo:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Lista com todos números:", intervalo)
print("Lista com os números pares:", pares)
print("Lista de números ímpares:", impares)
