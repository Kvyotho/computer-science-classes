"""
Construa uma função que receba uma lista de números e um número n.
A função deve retornar >outra lista< com >>n números maiores da lista<<.
+the returned list should not be sorted, however, further details will be given
later as to sorting the list, time complexity and algorithms
"""
# analise complexidade de algoritmo / time complexity
# big O and stuff
# think about solutions and problem solving, the core stuff of computer science
# solutions first, coding second
# always try to reduce algorithm complexity (=more efficiency!)


def n_max(n, lista):
    result = []
    c = 0
    max_index = 0
    while c < n:
        for numero in lista:
            if numero > max_index:
                max_index = numero
                result.append(numero)
                del numero
                c = c + 1 
        return result



print(n_max(3, [15, 21, 30, 20]))