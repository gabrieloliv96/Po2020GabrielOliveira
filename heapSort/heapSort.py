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

def geraLista(size):
    lista = list(range(1, size + 1))
    shuffle(lista)
    return lista

def heapsort(lista):
    for i in range(len(lista), -1, -1):
        heap(lista, len(lista), i)

    for i in range(len(lista)-1, 0, -1):
        aux = lista[i]
        lista[i] = lista[0]
        lista[0] = aux
        heap(lista, i, 0)

def heap(lista, size, atual):
    maior = atual
    esquerdo = 2 * atual + 1
    direito = 2 * atual + 2

    if esquerdo < size and lista[atual] < lista[esquerdo]:
        maior = esquerdo

    if direito < size and lista[maior] < lista[direito]:
        maior = direito

    if maior != atual:
        aux = lista[atual]
        lista[atual] = lista[maior]
        lista[maior] = aux
        heap(lista, size, maior)

size = [15000,25000,35000,45000,55000]
tempo = []

for i in range(5):
    lista = geraLista(size[i])
    tempo.append(timeit.timeit("heapsort({})".format(lista), setup="from __main__ import heapsort", number=1))

desenhaGrafico(size, tempo, "Tempo.png", 'size da lista de números', 'Tempo para ordenar pelo método')
