import numpy as np
import matplotlib.pyplot as plt

### 1 ###
ar = np.arange(1,11).reshape(2,5)
print(ar)
print()

### 3 ###
ar = np.arange(0,51)
cond_even = (np.mod(ar, 2) == 0)
cond_multi5 = (np.mod(ar, 5) == 0)
cond_both = cond_even | cond_multi5
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
print()

### 10 ###
ar = np.random.normal(170, 10, 100)

print(ar)
print(np.percentile(ar, 25))
print(np.percentile(ar, 50))
print(np.percentile(ar, 75))

print(f'A quantidade de pessoas com altura acima de 180 cm é: ', np.sum(ar > 180))

plt.hist(ar, bins=10, color='lightblue', edgecolor='black')
plt.title("Distribuição de Alturas")
plt.xlabel("Altura (cm)")
plt.ylabel("Frequência")
plt.show()

### 13 ###
ar1 = np.arange(1,6)
ar2 = np.arange(1,6)

ar1 = np.sqrt(ar1)
ar_result = ar1 - ar2
print(ar1)
print(ar2)
print(ar_result)
print()

### 17 ###
ar = np.random.randint(0,11,9).reshape(3,3)
print(ar)
print(np.linalg.det(ar))
print(np.linalg.inv(ar))


### 21 ###
ar1 = np.random.randint(0,1,10)
ar2 = np.random.randint(1,2,5)
ar3 = np.identity(4)

print(ar1)
print(ar2)
print(ar3)

### 26 ###
ar = np.random.randint(0,11,30)
ar_unq, ar_unq_freq = np.unique(ar, return_counts=True)

print(ar)
print(f'Valores únicos:', ar_unq)
print(f'Frequencia dos valores:', ar_unq_freq)