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

def bucketSort(lista):
    comprimento = len(lista)
    cesta = [[] for _ in range(comprimento)]
    maior = max(lista)
    tam = maior/comprimento

    for i in range(comprimento):
        j = int(lista[i] / tam)
        if j != comprimento:
            cesta[j].append(lista[i])
        else:
            cesta[comprimento - 1].append(lista[i])

    for i in range(comprimento):
        insertionSort(cesta[i])

    listaOrdenada = []
    for i in range(comprimento):
        listaOrdenada = listaOrdenada + cesta[i]

    return listaOrdenada


def insertionSort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and atual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual


tam =  [15000,25000,35000,45000,55000]
tempo = []

for i in range(5):
    lista = geraLista(tam[i])
    tempo.append(timeit.timeit("bucketSort({})".format(lista), setup="from __main__ import bucketSort", number=1))

desenhaGrafico(tam, tempo, "Tempo.png", 'Tamanho da lista', 'Tempo para ordenar')
