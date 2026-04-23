
import random
import time

#start = time.()
#end = time.()
#duration = end - start

lista = [random.randint(0, 2000000) for _ in range(20000000)]

#Solução 1
def tem_duplicados1(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

start = time.time()
tem_duplicados1(lista)
end = time.time()
duration = end - start
print(f'A primeira solução levou {duration: .5f} segundos')


#Solução 2
def tem_duplicados2(lista):
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
    return False

start = time.time()
tem_duplicados2(lista)
end = time.time()
duration = end - start
print(f'A segunda solução levou {duration: .5f} segundos')

#Solução 3
def tem_duplicados3(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False

start = time.time()
tem_duplicados3(lista)
end = time.time()
duration = end - start
print(f'A terceira solução levou {duration: .5f} segundos')

"""
Saída Obtida:
A primeira solução levou  0.05089 segundos
A segunda solução levou  7.41017 segundos
A terceira solução levou  0.00000 segundos

Resposta correta: c) Abordagem 3 é mais eficiente em tempo, mas consome mais espaço

Resposta marcada: c) Abordagem 3 é mais eficiente em tempo, mas consome mais espaço

Analíse de erro: Nenhum

"""



