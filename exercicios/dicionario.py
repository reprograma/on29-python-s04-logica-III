notas_belisa = {
    "nota1": 5,
    "notas2": 10
}
# trazendo os nomes
for nota in notas_belisa:
    print(nota)
# trazendo os valores
for nota in notas_belisa.values():
    print(nota)
# trazendo nomes e valores
for nota in notas_belisa.items():
    print(nota)
# trazendo nomes e valores separados
for nome, valor in notas_belisa.items():
    print(nome)
    print(valor)
