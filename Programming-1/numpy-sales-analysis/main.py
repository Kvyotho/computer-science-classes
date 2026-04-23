import numpy as np
import datetime

#### 1 Leitura e Preparação dos Dados: ###
data = np.genfromtxt('vendas.csv', dtype=[
    ('Data','datetime64[D]'),
    ('Região', 'U5'),
    ('Produto', 'U10'),
    ('Quantidade Vendida', 'i4'), 
    ('Preço Unitário', 'f8' ),
    ('Valor Total', 'f8')
    ], 
    delimiter=',', skip_header=1)


valor_total = data['Valor_Total']

### 2. Análise Estatística: ###
#Calcule a média, mediana e desvio padrão do Valor Total das vendas.
print(f'A média do Valor total de vendas é: {np.mean(valor_total):.2f}')
print(f'A mediana do Valor total de vendas é: {np.median(valor_total):.2f}')
print(f'O desvio padrão do Valor total de vendas é: {np.std(valor_total):.2f}')
print('')


#Encontre o produto com a maior quantidade vendida
index_mqv = np.argmax(data['Quantidade_Vendida'])
produto_mqv = data['Produto'][index_mqv]
print(f'O produto com a maior quantidade vendida é: {produto_mqv}')


#Encontre o produto com o maior valor total de vendas.
index_mvv = np.argmax(data['Valor_Total'])
produto_mvv = data['Produto'][index_mvv]
print(f'O produto com o maior valor total de vendas é: {produto_mvv}')
print('')


#Calcule o valor total de vendas por região.
vt_norte = np.sum(data['Valor_Total'][data['Região'] == 'Norte'])
vt_sul = np.sum(data['Valor_Total'][data['Região'] == 'Sul'])
vt_leste = np.sum(data['Valor_Total'][data['Região'] == 'Leste'])
vt_oeste = np.sum(data['Valor_Total'][data['Região'] == 'Oeste'])

print(f'Valor total de vendas na região Norte: {vt_norte:.2f}')
print(f'Valor total de vendas na região Sul: {vt_sul:.2f}')
print(f'Valor total de vendas na região Leste Leste: {vt_leste:.2f}')
print(f'Valor total de vendas na região Oeste: {vt_oeste:.2f}')
print('')


#Determine a venda média por dia.
dias_unicos = np.unique(data['Data'])
soma_vendas_por_dia = [np.sum(data['Quantidade_Vendida'][data['Data'] == date]) for date in dias_unicos]

print(f'A média de vendas por dia é: {np.mean(soma_vendas_por_dia):.2f}')
print('')

### 3. Análise Temporal: ###
#Determine o dia da semana com maior número de vendas.
dias_da_semana = data['Data'].astype('datetime64[D]').view('int64') % 7
venda_por_dia_semana = [np.sum(data['Quantidade_Vendida'][dias_da_semana == day]) for day in range(7)]
dia_com_maior_vendas = np.argmax(venda_por_dia_semana)


dicionario_dias = {
    0: 'Segunda-feira',
    1: 'Terça-feira',
    2: 'Quarta-feira',
    3: 'Quinta-feira',
    4: 'Sexta-feira',
    5:'Sábado',
    6: 'Domingo'
    }
print(f'O dia da semana com o maior número de vendas é: {dicionario_dias[dia_com_maior_vendas]}')


#Calcule a variação diária no valor total de vendas, ou seja, a diferença entre as vendas de um dia e o dia seguinte.
valor_total_por_dia = [np.sum(data['Valor_Total'][data['Data'] == date]) for date in dias_unicos]
variacao_diaria = np.diff(valor_total_por_dia)
print(f'A variação diária do valor total de vendas é: {np.mean(variacao_diaria):.2f}')
