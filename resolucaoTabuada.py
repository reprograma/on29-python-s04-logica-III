# Tabuada 
# ler o número da tabuada 
tabuada = int(input('Deseja fazer a tabuada de qual número: '))
# definir o começo
inicio = int(input('Deseja que inicie com qual número: '))
# definir o final
fim = int(input('Deseja termine em qual númmero: '))
# testar se o início é manor que o final

if inicio > fim :
    print('O início deve ser menor do que o final.')
else:
     # enquanto iníco for menor que fim
    while inicio <= fim : # não está testando 
        # mostrar tabuada x início 
        print(f'{tabuada} x {inicio} = {tabuada * inicio}')
        # acrescentar + 1 no início para modificar as multiplicações
        inicio += 1
    print('Resultado impresso.')
    print('Fim!')

