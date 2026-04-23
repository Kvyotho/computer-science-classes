import numpy as np
'''
as dimensoes do caso base A.shape == (1,1) e *A[0, j] podem ser diferentes
ex: A.shape == (2,2 e *A[?, j])
'''

def det(A):
    
    #caso base
    if A.shape == (1, 1):
        return A[0, 0]

    result = 0
    for j in range(A.shape[1]):
        sub = np.delete(np.delete(A, 0, 0), j, 1)
        result += ((-1)**(1 + (j+1))) * A[0, j] * det(sub)

    return result


matrix = np.array([
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
])

print(matrix)
print('O detemrinante é> ', + det(matrix))

    
#Exercicio de Cramer

import numpy as np

'''
exemplo do sistema utilizado
x + 2y + z  = 12
x - 3y + 5z = 1
2x - y + 3z = 10
'''

sistema = np.array([
    [1,2,1,12],
    [1,-3,5,1],
    [2,-1,3,10]
])

def cramer(sistema):


print('Os índices são: ', cramer(sistema))
