tabuada = int(input('Tabuada do: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar por: '))
#final não pode ser menor que o inicial

if inicio < fim:
    while inicio <= fim:
        resultado = tabuada * inicio
        print('{} x {} = {}'.format(tabuada, inicio, resultado))
        inicio = (inicio + 1)
else:
    print('Você precisa escolher um número para começar menor que o número para terminar a tabuada!')
