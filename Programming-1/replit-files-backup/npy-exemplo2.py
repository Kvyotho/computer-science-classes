import numpy as np

#shapes
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

print(arr.shape)

numeros = np.arange(15)
print(numeros)
numeros = numeros.reshape(3,5)
print(numeros)

numeros = np.arange(18)
print(numeros)
lm = numeros.reshape(2,3,3) #very useful for neural net, dealing with dimensions and stuff
print(lm)

numeros = np.arange(24)
print(numeros)
lm = numeros.reshape(2,3,-1) #-1 means it will discover a dimension for you,
print(lm)                    #so you can trial and error in np.arrange(24)
print(lm.shape)
