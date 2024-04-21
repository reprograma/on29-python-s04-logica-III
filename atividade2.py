def main():
    numeros = []
    pares = []
    impares = []
    
    print("Digite 20 números inteiros:")
    for _ in range(20):
        try:
            numero = int(input("> "))
            numeros.append(numero)
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
        except ValueError:
            print("Por favor, insira apenas números inteiros. Tente novamente.")
            return

    print("Vetor de números lidos:", numeros)
    print("Vetor de números pares:", pares)
    print("Vetor de números ímpares:", impares)

main()