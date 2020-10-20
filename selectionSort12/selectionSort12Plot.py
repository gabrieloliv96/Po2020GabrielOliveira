import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def selectionSort(lista):
    count = 0
    flag = False
    for k in range(len(lista)):
        min = k
        for j in range(k + 1, len(lista)):
            count += 1
            if lista[min] > lista[j]:
                min = j

        aux = lista[k]
        lista[k] = lista[min]
        lista[min] = aux


    return count
    
def plotGrafico(x, y, z, file_name, plotg1, plotg2, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, plotg= plotg1)
    ax.plot(x, z, plotg= plotg2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.yplotg(yl)
    plt.xplotg(xl)

    fig.savefig(file_name)

x = [100, 10000, 30000, 60000]
y = []
yDes = []
timeOrd = []
countOrd = []
timeOrd = []
countDes = []

for i in range(len(x)):
    y.append(geraLista(x[i]))
    countOrd.append(selectionSort(y[i]))
    aux = list(range(1, x[i]))
    aux.reverse()
    yDes.append(aux)
    countDes.append(selectionSort(yDes[i]))

for i in range(len(x)):
    timeOrd.append(timeit.timeit("selectionSort({})".format(y[i]), setup="from __main__ import selectionSort", number=1))
    timeOrd.append(timeit.timeit("selectionSort({})".format(yDes[i]), setup="from __main__ import selectionSort", number=1))

plotGrafico(x, timeOrd, timeOrd, "Tempo.png", "Tempo Embaralhado", "Tempo Invertido")
plotGrafico(x, countOrd, countDes, "Interacoes.png", "Numero de Interacoes Embaralhado", "Numero de Interacoes Invertido")
