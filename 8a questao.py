
def bmi_calc(weight, height):
    
    bmi = weight / (height * height)

    if bmi < 17:
        print(f'Seu IMC é: {bmi:.2f}, classificado como Muito abaixo do peso')
    elif bmi < 18.5:
        print(f'Seu IMC é: {bmi:.2f}, classificado como Abaixo do peso')
    elif bmi < 25:
        print(f'Seu IMC é: {bmi:.2f}, classificado como Peso normal')
    elif bmi < 30:
        print(f'Seu IMC é: {bmi:.2f}, classificado como Sobrepeso')
    elif bmi < 35:
        print(f'Seu IMC é: {bmi:.2f}, classificado como Obesidade grau I')
    elif bmi < 40:
        print(f'Seu IMC é: {bmi:.2f}, classificado como Obesidade grau II')
    else:
        print(f'Seu IMC é: {bmi:.2f}, classificado como Obesidade grau III')

weight = float(input("Informe seu peso em kg: "))
height = float(input("Informe sua altura em metros: "))
bmi_calc(weight, height)

"""
Saída Obtida: 

Resposta correta: 

Resposta marcada: 

def bmi_calc(weight, height)
    bmi = 0
    bmi = (weight / (height*height))
    return bmi
        if bmi <17:
            print(f'Seu IMC é: (bmi), classificado como muito abaixo do peso', bmi)
        elif bmi <18.5:
            print(f'Seu IMC é: (bmi), classificado como abaixo do peso', bmi)     
        elif bmi <25:
            print(f'Seu IMC é: (bmi), classificado como peso normal', bmi)
        elif bmi <30:
            print(f'Seu IMC é: (bmi), classificado como sobrepeso', bmi)     
        elif bmi <35:
            print(f'Seu IMC é: (bmi), classificado como obesidade grau I', bmi)
        elif bmi <40:
            print(f'Seu IMC é: (bmi), classificado como obesidade grau II', bmi)     
        else:
            print(f'Seu IMC é (bmi), classificado como obesidade grau III', bmi)
    

Analíse de erro: 

-Iniciei BMI = 0 de forma desncessaria

-Retornei BMI no começo/meio da função (Acho que nesse erro escrevi parte do rascunho na resposta final sem querer)

-Não utilizei .2f para representar números com quebrados como no 18.5

-Utilizei (bmi) ao invés de {bmi} na string formatada, e adicionei (bmi) denovo após fechar o '' da string, de forma desnecessária

-Provavelmente existe como refatorar esse código para deixar ele mais eficiente/limpo

-Só fiz a função de calculo do BMI, não implementei um código inteiro com input, pedindo ao usuário o peso e a altura
"""