import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def desenhaGrafico(x, y, y2, figura, xLabel ="Entradas", yLabel ="Saídas"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista aleatória")
    
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)
    plt.show()

def geraLista(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista

def listaDecrescente(tamanho):
    lista = list(range(1, tamanho + 1))
    lista.reverse()
    return lista

def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esq = lista[:meio]
        dir = lista[meio:]
        mergeSort(esq)
        mergeSort(dir)

        i = 0
        j = 0
        k = 0

        while i < len(esq) and j < len(dir):
            if esq[i] < dir[j]:
                lista[k] = esq[i]
                i += 1
            else:
                lista[k] = dir[j]
                j += 1
            k += 1

        while i < len(esq):
            lista[k] = esq[i]
            i += 1
            k += 1

        while j < len(dir):
            lista[k] = dir[j]
            j += 1
            k += 1

tamanho = [20000,40000,60000,80000,100000]
tempo = []
tempo2 = []

for i in range(5):
    lista = geraLista(tamanho[i])
    lista2 = listaDecrescente(tamanho[i])
    tempo.append(timeit.timeit("mergeSort({})".format(lista), setup="from __main__ import mergeSort", number=1))
    tempo2.append(timeit.timeit("mergeSort({})".format(lista2), setup="from __main__ import mergeSort", number=1))

desenhaGrafico(tamanho, tempo, tempo2, "Tempo.png", 'Tamanho da lista', 'Tempo gasto')
