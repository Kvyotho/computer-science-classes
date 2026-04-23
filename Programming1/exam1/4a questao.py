lista = [1, [2,3], 4]
print(lista[1][1])

"""
Saída Obtida: 3

Resposta correta: c) 3 

Resposta marcada: e) Erro de Índice(IndexError)

Analíse de erro: Apesar de ter quase certeza que isso também foi demonstrado em sala (acessar uma lista dentro de outra lista), por algum
motivo, eu não achei que isso seria possível, e marquei a opção de IndexError

Salvo engano, minha linha de raciocinio durante a prova foi de que print(lista[1][1]) tentaria acessar a coluna index 1 da lista[], sendo que
só existe a coluna index 0. 

Porém dentro da lista na lista[2,3], existe de fato a coluna 0 (2) e a coluna 1(3), sendo assim acessível o elemento
1 da lista[] ([2,3]) e a coluna 1 desse elemento (3)

"""
