tabuada = int(input("Montar a tabuada de: "))
inicio = int(input("Começando em: "))
fim = int(input("Terminando em: "))

for i in range(inicio, fim+1):
  print(f"{tabuada} X {i} = {tabuada*i}")