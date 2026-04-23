# Problema nº 1: Duas Somas
# O problema é encontrar dois números em uma lista que somam um
# determinado número alvo. Precisamos retornar os índices desses dois 
# números em qualquer order. Podemos assumir que existe apenas uma 
# solução válida e não podemos usar o mesmo elemento duas vezes:


def coordenadas_soma(lista, valor):
    n1 = 0 
    n2 = 0

    while n1 < len(lista):
        n2 = n1 + 1
        while n2 < len(lista): 
            if (lista[n1]+lista[n2]) == valor:
                return (n1, n2)
            n2 += 1
        n1 += 1
    
    raise Exception("Par não encontrado")

def coordenadas_soma_otima(lista, valor):
    complementos = {}

    for n in range(len(lista)):
        #print(complementos)
        try:
            if(complementos[lista[n]]):
                return (n, complementos[lista[n]])
        except Exception:
            complementos[valor-lista[n]] = n
    
    raise Exception("Pares não localizados")


numeros = [5, 2, 3, 1, 6, 7]
soma_10 = coordenadas_soma(numeros, 10)
print(soma_10)
soma_10 = coordenadas_soma_otima(numeros, 10)
print(soma_10)



