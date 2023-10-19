import random

def gera_resultados(): #gerar um placar
    pontosA = random.randint(75,130)
    pontosB = random.randint(75,130)
    while pontosA == pontosB:
        pontosB = random.randint(75,130)
    return [pontosA, pontosB]

def eliminatorias(timeA, timeB, arquivo):
    vitoriasA = 0
    vitoriasB = 0
    while vitoriasA < 4 and vitoriasB < 4:
        placar = gera_resultados()
        arquivo.write(f"{timeA} {placar[0]} X {placar[1]} {timeB}\n")
        if placar[0]> placar[1]:
            vitoriasA +=1
        else:
            vitoriasB += 1
    if vitoriasA == 4:
        return timeA
    else:
        return timeB
 

leste = ["Knicks", "Mets", "Celtis", "Bucks", "Cavaliers", "765Sixers", "Hornets", "Bulls"]

oeste = ["Lakers", "Wariors", "Nuggets", "Suns", "Grizzlers", "Heat", "Raptors", "Clippers"]

arq = open("resultado.txt", "w")

while len(leste) > 1:

    aux_leste = []
    aux_oeste = []

    i = 0
    j = len(leste) - 1

    while i < j:
        vencedor = eliminatorias(leste[i], leste[j], arq)
        aux_leste.append(vencedor)
        vencedor = eliminatorias(oeste[i], oeste[j], arq)
        aux_oeste.append(vencedor)

        i +=1
        j -=1

    leste = aux_leste
    oeste = aux_oeste

vencedor = eliminatorias(leste[0], oeste[0], arq)

print('Vencedor: ', vencedor)

arq.close()