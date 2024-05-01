###Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
#o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:


n0= int(input("Para qual número deseja montar a tabuada?")) # numero que será montada a tabuada
n1= int(input("Começa por: ")) # numero que comecarpa a tabuada
n2= int(input("Termina em: ")) # numero que terminará

print("Será montada a tabuada do",n0,".\nE começará em", n1, "e terminará em", n2,".\nSegue tabuada:")

for multiplicador in range(n1, n2 +1): # itera sobre cada multiplicador de n1 até n2
    resultado = n0 * multiplicador # aqui multiplica
    print(f"{n0} X {multiplicador} = {resultado}") # imprime o resultado

print("Fim do programa........")

