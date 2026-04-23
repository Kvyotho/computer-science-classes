'''
path 1: just search
path 2: complement dictionary, list
-only 1 loop
-may finish even before a single loop
create a dict, with complements of the elements, and return the index1 and index2, where/if i1+i2=value
path 3: transform each element of the list into something else, e.g: tupla,
then sort the list by ascending order
then search by left and then right
the sum (X,y), (x,y), (x,y), (x,y), (x,y), (x,Y) -> sum (X,Y)
'''
import random
import time


def soma_n4(lista, valor):
    lt = [(lista[i], i) for i in range(len(lista))]
    lt = sorted(lt, key=lambda x: x[0])

    x = 0
    y = len(lista)
    while x != y:
        if lt[x][0] + lt[y][0] == valor:
            return (x, y)
        elif lt[x][0] + lt[y][0] > valor: 
            y -= 1

            x += 1           

def soma_n3(lista, valor):
    complementos = {}
    for i in range(len(lista)):
        try:
            return (i, complementos(lista[i]))
        except:
            complementos.update({valor - lista[i: i]})

def soma_n2(lista, valor):
    complementos = {}
    for i in range(len(lista)):
        if complementos[lista[i]]:
            return (i, complementos[i])
        else:
            complementos.update({valor - lista[i]: i})

def soma_n(lista, valor):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == valor:
                return (i, j)

    return (0,0)

for quantidade in range(10000, 100001, 10000):
    total_1 = 0
    total_2 = 0
    numeros = [random.randint(1, 1000000000) for _ in range(quantidade)]
    for round in range(10):
        aleatorios = random.sample(numeros, 2)


numeros = [5, 3, 1 ,8 ,4 ,7 ,9]
print(soma_n(numeros, 10))