# Desenvolvendo um programa que faça a tabuada de um número qualquer. O número será o 3

num1 = int(input("Digite o início: "))
num2 = int(input("Digite o final: "))
num3 = int(input("Tabuada para o número: "))
sequencia = range(num1, num2 + 1)

while int(num1) <= int(num2):

    num1 = int(num1) + 1

for num1 in sequencia:
    resultado = num3 * num1
    print("Resultado de " + str(num3) + " x " + str(num1) + " = " + str(resultado))
    
print("FIM DO PROGRAMA")
