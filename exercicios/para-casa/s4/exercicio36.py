#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
#o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
def multiplicar():
    while True:
        num1 = int(input("Fazer a tabuada de: "))
        num2 = int(input("Começar por: "))
        num3 = int(input("Terminar por: "))

        if num3 >= num2:
            break
        else:
            print(f"ERRO. O valor informado {num2} é maior que {num3}. Tente novamente")
    for i in range(num2, num3+1): #aqui num2 é o start e o num3 é o stop do range(start, stop, step), step sempre fica subentendido que será 1.
        resultado = num1 * i
        print(f"{num1} x {i} = {resultado}")

multiplicar()
