alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))
if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)


"""
Saída Obtida: 

1)
Informe X: 1
1.0

2)
Informe alpha: 0.2
Informe X: 1
Valor inválido para alpha

3)
Informe alpha: 0.1
Informe X: 0.3
0.3

4)
Informe alpha: 0.1
Informe X: 0
0.0

Resposta correta: ?

Resposta marcada: "Não, o código não vai produzir a sáida adequada para todas as diferentes entrades de alpha e x,
conforme demonstrado no terceiro teste, o valor excede 0.1"

Analíse de erro: Errei no primeiro teste, confundindo x < 0 com x > 0, e gerando o output errado.


Acredito que errei na justificativa devido aos seguintes motivos:

-O enunciado da questão pergunta apenas em relação ao valor de alpha, eu respondi sobre o valor final que o código gera.

-Não especifiquei qual valor excede 0.1.

-Justifiquei errado, pois o valor de alpha vai exceder ou não, conforme o input de alpha do usuario,
porém, caso exceda, o código está escrito corretamente para identificar e gerar um print de erro.
"""