
import numpy as np
import matplotlib.pyplot as plt

'''
1. Crie dois arrays Numpy de 10 elementos cada, preenchidos com numeros inteiros aleatorios. 
Calcule a soma, a diferença, o produto e a divisão element-wise entre eles.
'''

ar1 = np.random.randint(1,10,size=10)
ar2 = np.random.randint(1,10,size=10)
print(' ----\n1. Questão\n ----')
print(ar1)
print(ar2)

soma_ar = np.add(ar1, ar2)
print(f'Soma', soma_ar)

sub_ar = np.subtract(ar1, ar2)
print('Diferença', sub_ar)

prod_ar = np.multiply(ar1, ar2)
print(f'Produto',prod_ar)

div_ar = np.divide(ar1, ar2)
print(f'Divisão',div_ar)

'''
2. Crie duas matrizes 3x3 com numeros aleatorios.
Realize a multiplicação de matrizes (dot product) e calcule a transposta da matriz resultado.
'''
ar1 = np.random.randint(1, 10, size=(3, 3))
ar2 = np.random.randint(1, 10, size=(3, 3))
print(' ----\n2. Questão\n ----')
print(ar1)
print(ar2)

print(np.dot(ar1, ar2))
print(np.transpose(np.dot(ar1, ar2)))

'''
3.Crie dois arrays de 10 elementos com numeros aleatorios.
Compare os arrays  e crie um novo array booleano que indique onde os elementos são iguais.
'''
ar1 = np.random.randint(1,10,size=10)
ar2 = np.random.randint(1,10,size=10)

print(' ----\n3. Questão\n ----')
print(ar1)
print(ar2)
print(np.equal(ar1, ar2))

'''
4.Crie um array 2D de forma (4,3) e um array 1D de forma (3,). 
Utilize broadcasting para somar os dois arrays.
Apresente o resultado.
'''

ar1 = np.random.randint(1, 10, size=(4, 3))
ar2 = np.random.randint(1,10,size=3)

print(' ----\n4. Questão\n ----')
print(ar1)
print(ar2)
print(ar1 * ar2)

'''
5.Gere 1000 numeros aleatorios (entre 0 e 100) de uma distribuição.
Utilize NumPy para calcular o histograma desses dados e exiba 
os resultado s em um gráfico utilizando um gráfico de barras do matplotlib.
'''






