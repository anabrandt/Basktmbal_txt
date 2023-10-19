with open('resultado.txt', 'r') as arq:
    for jogo in arq:
        info = jogo.replace("\n", '').split()
        print(jogo)
