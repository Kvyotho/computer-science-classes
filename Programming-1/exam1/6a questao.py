matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

#A)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma
print(soma_diagonal_principal(matriz))


#B)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-i]
    return soma
print(soma_diagonal_principal(matriz))


#C)
def soma_diagonal_principal(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma
print(soma_diagonal_principal(matriz))


#D)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz)-i-1]
    return soma
print(soma_diagonal_principal(matriz))


#E)
def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz)-i-1][i]
    return soma
print(soma_diagonal_principal(matriz))

"""
Saída Obtida: 
A) 15
B) 15
C) 45
D) 15
E) 15

Resposta correta: a)

Resposta marcada: a)

Analíse de erro: Nenhum

"""
