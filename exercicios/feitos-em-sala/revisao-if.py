nota_da_aluna = 10

media = 6
nota_minima_para_recuperacao = 3

if nota_da_aluna >= media:
    print("Aprovada!")
elif nota_da_aluna >= nota_minima_para_recuperacao: 
    print("Recuperação :( )")
else:
    print("Reprovada :'( )")