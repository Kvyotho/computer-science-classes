
#A
lista = [x for x in range(5)]
print(lista)

#B
lista = list(range(5))
print(lista)

#C
lista = []
i = 0
while i < 5:
    lista.append(i)
    i += 1
print(lista)

"""
Saída Obtida:
A) [0, 1, 2, 3, 4]
B) [0, 1, 2, 3, 4]
C) [0, 1, 2, 3, 4]

Resposta correta: d) Todos os códigos A, B e C (produzem o mesmo resultado)

Resposta marcada: e) Nenhum dos códigos produz o mesmo resultado

Analíse de erro: 
A) Achei que o código não iria executar corretamente, mas é só list comprehension básica

B) Achei que iria gerar uma lista de 0 até 5

C) Achei (finalmente desta vez acertando) que iria gerar uma lista do 0 até o 4, com o loop while
começando em 0 e parando uma vez que chegasse ao 5, logo não executando o lista.append(i) com o número 5

Com base nessas três suposições, marquei a opção e)

"""
