import numpy as np

lista_normal = [5, 3 ,2 ,8 ,9]
array = np.array(lista_normal, dtype=int) #caso não colocar dtype, ele infere auto

'''
print(lista_normal)
print(type(lista_normal))
print(array)
print(type(lista_normal))
print(array.dtype)
'''

#Dimensions

ar1 = np.array(42)
print(ar1)

ar2 = np.array([1,2,3])
print(ar2)
print(ar2.ndim)

ar3 = np.array([
    [1,2,3],
    [4,5,6]
])

print(ar3)
print(ar3.ndim)

ar4 = np.array([[
    [1,2,3],
    [4,5,6]
],
[
    [1,2,3],
    [4,5,6]
]])

print(ar4)
print(ar4.ndim)

ar = np.array([1,2,3], ndmin=5)

print(ar)
print(ar.ndim)

#index
ar6 = np.array([1,2,3])
print(ar6[1])

arr = np.array([1,2,3])
print(arr[1])

#slicing
lista = np.arange(15)
print(lista)

pedaco = lista[5:9] #in order to not change the original list, just add .copy() at the end [5:9].copy()
print(pedaco)

pedaco[0] = 69 #ponteiro, afeta a lista original
print(pedaco)
print(lista) 

pedaco2 = lista[-5:]
print(pedaco2)


#data types

frutas = np.array(('banana', 'maça', 'morango', 'laranja'))
print(frutas)
print(frutas.dtype)

numeros = np.array([1,2,3,4], dtype='i8')
print(numeros)
print(numeros.dtype)

newarr = np.array([1.1 ,2.1, 3.1], dtype='i')
print(newarr)
print(newarr.dtype)