import numpy as np

### 1 ###
ar = np.arange(1,11).reshape(2,5)
print(ar)
print()
### 2 ###

ar1 = np.random.randint(1,100,10)
ar2 = np.random.randint(1,100,10)

ar_soma = ar1 + ar2
ar_sub = ar1 - ar2
ar_mult = ar1 * ar2
ar_div = ar1 / ar2
print(ar1)
print(ar2)
print(f'Soma:',ar_soma)
print(f'Subtração:',ar_sub)
print(f'Multiplicação:',ar_mult)
print(f'Divisão:',ar_div)
print()

### 3 ###
ar = np.arange(0,51)
cond_even = (np.mod(ar, 2) == 0)
cond_multi5 = (np.mod(ar, 5) == 0)
cond_both = cond_even | cond_multi5

print(np.extract(cond_both, ar))

### 4 ###
ar = np.random.randint(0,2,20)

print(ar)
print(f'Média:', np.mean(ar))
print(f'Desvio padrão:', np.std(ar))
print(f'Valor máximo:', np.argmax(ar))
print(f'Valor mínimo:', np.argmin(ar))

### 5 ###
ar = np.arange(1,17).reshape(4,4)
ar_tps = np.transpose(ar)
ar_mult = ar * ar_tps

print(ar)
print(ar_tps)
print(ar_mult)

### 6 ###
ar = np.arange(1,100,20)
print(ar)
np.place(ar,ar>50, 0)
print(ar)
print()

### 7 ###
ar = np.random.randint(1,11,20).reshape(5,4)
print(ar)

print(f'Média do 1º Aluno:', np.mean(ar[0]))
print(f'Média do 2º Aluno:', np.mean(ar[1]))
print(f'Média do 3º Aluno:', np.mean(ar[2]))
print(f'Média do 4º Aluno:', np.mean(ar[3]))
print(f'Média do 5º Aluno:', np.mean(ar[4]))
print()
print(f'Média da 1ª Prova', np.mean(ar[:, 0]))
print(f'Média da 2ª Prova', np.mean(ar[:, 1]))
print(f'Média da 3ª Prova', np.mean(ar[:, 2]))
print(f'Média da 4ª Prova', np.mean(ar[:, 3]))

### 8 ###
ar = np.random.randint(0,11,9).reshape(3,3)
print(np.linalg.eigh(ar))

### 9 ###

### 10 ###
ar = np.random.randint(160,181,100)
print(ar)