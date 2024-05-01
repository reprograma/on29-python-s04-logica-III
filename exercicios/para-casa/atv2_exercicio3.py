###Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

tamanho= 20

# declarar as variaveis em uma lista vazia para chamá-las posteriormente
num= []
pares= []
impares= []
posicao= 1

print("Informa os números abaixo: ")

for posicao in range(tamanho): # loops para receber os 20 numeros
    nums= int(input(f"Digite o {posicao}° número: "))
    num.append(nums) # adiciona o numero informado na lista vazia declarada acima
    
    if nums % 2 == 0: # esse tipo de divisao retorna o resto e será usada para identificar se é par, ou ímpar
        pares.append(nums) # resto 0 adiciona a lista par
    else:
        impares.append(nums) # se tiver resto, adiciona a lista impar
        
print("\nNúmeros digitados: ", num)
print("Números pares: ", pares)
print("Números ímpares: ", impares)
    

