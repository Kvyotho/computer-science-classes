import numpy as np
import matplotlib.pyplot as plt

#next week activities based on these concepts
#rewarding points xdd

temperaturas = np.random.randint(15, 35, size=30)

#print(temperaturas)

print(temperaturas)

#Calcule a temperatura média do mês
print(f'A média é: {np.mean(temperaturas, dtype=float):.2f}°C.') 

#Identifique a temperatura mais alta e a mais baixa
print(f'A temperatura mínima é: {np.min(temperaturas):.2f}°C')
print(f'A temperatura máxima é: {np.max(temperaturas):.2f}°C')

#Calcule a mediana das temperaturas
print(f'A mediana é: {np.median(temperaturas):.2f}°C')

'''
>>Manipulação de Dados
Apresentar uma lista contendo apenas as ocorrências de temperatura
iguais ou superiores a 30°C.
'''
print(temperaturas[temperaturas >= 30])

'''
Crie uma nova lista das temperaturas na escala Fahrenheit
tf = tc*9/5 + 32
'''
temperaturas_fh = temperaturas*9/5 + 32
print(temperaturas_fh)


#Gráfico das temperaturas
plt.plot(temperaturas, marker='o')
plt.title('Temperaturas diárias ao longo do mês')
plt.xlabel('Dia')
plt.ylabel('Temperatura (oC)')
plt.show()

semanas = np.array_split(temperaturas, 4)
print(semanas)

medias_semanais = [np.mean(semana) for semana in semanas]
print(medias_semanais)

plt.bar(range(1,5), medias_semanais, color=['red', 'blue', 'yellow', 'green'])
plt.title('Média das Temperaturas')
plt.xlabel('Semana')
plt.ylabel('Temperatura média (oC)')
plt.xticks(range(1,5), ['Semana 1','Semana 2','Semana 3','Semana 4'])
plt.show()

