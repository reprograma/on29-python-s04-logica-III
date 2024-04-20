print("exercício 1: Crie um código que imprima todos os número inteiros entre 0 e 10")
sequencia1 = range(11)
print(sequencia1)
for item in sequencia1:
    print(item)

print("exercício 2:Crie um código que imprima todosos número inteiros entre 10 e 0 ")
sequencia2 = range(10, -1, -1)
# start só pode ser maior que stop, se estivermos indo decrescente. dai a step tem que ser negativa. ex -1
for item2 in sequencia2:
    print(item2)

print("exercício 3: Crie um código que imprima todos os número inteiros entre 10 e 0")
sequencia3 = range(24, 69, 2)
for item3 in sequencia3:
    print(item3)

print("exercício 4: Crie um código que imprima a soma de todos os números entre 0 e 10")
sequencia4 = range(0, 11, 1)
soma = 0
for item4 in sequencia4:
    soma = soma + item4
print(soma)

print("exercício 5: Crie um código que conte as letras do seu nome")
soma_nome = 0
for nome in "Ana Paula":
    soma_nome = soma_nome + 1
    print(nome)
print(soma_nome)


print(len('Ana Paula'))
# biblioteca len conta quantos caracteres tem
