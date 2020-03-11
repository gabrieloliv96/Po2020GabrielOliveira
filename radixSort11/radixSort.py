  
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def desenhaGrafico(x, y, figura, xLabel ="Entradas", yLabel ="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)

def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista

def radixSort(lista):
    base = 1
    maior = max(lista)

    while maior/base > 0:
        indice = len(lista) + 1
        rpt = [0] * indice

        for i in lista:
            rpt[i] += 1

        k = 0

        for i in range(indice):
            for j in range(rpt[i]):
                lista[k] = i
                k += 1
        base *= 10


tam = [20000,30000,40000,50000,60000]
tempo = []

for i in range(5):
    lista = geraLista(tam[i])
    tempo.append(timeit.timeit("radixSort({})".format(lista), setup="from __main__ import radixSort", number=1))

desenhaGrafico(tam, tempo, "Tempo.png", 'Tam da lista', 'Tempo de Ordenação')
