def montar_tabuada(base, inicio, fim):
    if fim < inicio:
        print("O valor final não pode ser menor que o valor inicial.")
        return

    print(f"Vou montar a tabuada de {base} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        print(f"{base} X {i} = {base * i}")

def main():
    try:
        base = int(input("Montar a tabuada de: "))
        inicio = int(input("Começar por: "))
        fim = int(input("Terminar em: "))
        
        montar_tabuada(base, inicio, fim)

    except ValueError:
        print("Por favor, digite apenas números inteiros.")
main()