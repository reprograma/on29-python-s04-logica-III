# Criar uma lista
lista = []
# Criar a variável para receber os números 
numero = 0
par = []
impar = []
# Adiconar 20 itens na lista
for a in range(1, 21):
    numero = int(input(f'Digite o {a}° valor: '))
    lista.append(numero) # adicionando os números na lista 
    # Armazenar os pares em um vetor par 
    if numero % 2 == 0:
        par.append(numero) # adicionando os pares na lista par
    # Armazenar os ímpares em um vetor ímpar 
    else:
        impar.append(numero) # adicionando os ímpares na lista ímpar 
# Imprimir as três listas
print(f'Os valores digitados foram {lista}\nDessa lista os números {par} são pares\nE os números {impar} são ímpares.')



