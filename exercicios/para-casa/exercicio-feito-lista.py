num = int(input("Digite um dígito de número: "))

par = []
impar = []

for i in range(20):
    if num % 2 == 0:
        par.append(num)
        print("Lista de números pares: ", par)
    else:
        impar.append(num)
        print("Lista de números ímpares: ", impar)
