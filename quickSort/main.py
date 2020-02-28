import random
import timeit
import matplotlib.pyplot as plt

def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

def frag(lista, ini, fim):
    pivo = lista[fim - 1]
    for i in range(ini, fim):
        if not lista[i] > pivo:
            lista[ini], lista[i] = lista[i], lista[ini]
            ini += 1
    return ini-1

def quickSort(lista, ini, fim):
    if ini < fim:
        pivo = pivoRand(lista, ini, fim)
        quickSort(lista, ini, pivo)
        quickSort(lista, pivo + 1, fim)
    return lista

def pivoRand(lista, ini, fim):
    rand = random.randrange(ini, fim)
    lista[fim - 1], lista[rand] = lista[rand], lista[fim - 1]
    return frag(lista, ini, fim)

tam = [100000,200000,300000,400000,500000]
times = []

for i in range(len(tam)):
    listaInvertida = list(range(tam[i], 0, -1))
    times.append(timeit.timeit("quickSort({}, {}, {})".format(listaInvertida, 0, len(listaInvertida)),
                               setup="from __main__ import quickSort, pivoRand, frag", number=1))

desenha_grafico(tam, times, "Tempo.png", "Tempo gasto pelo quickSort", xl="Tamanho da lista", yl="Tempo")
