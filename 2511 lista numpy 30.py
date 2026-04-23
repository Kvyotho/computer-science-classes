import numpy as np
import numpy.ma as ma

### 11 ###

ar = np.arange(0,21)
print(ar.dtype)
ar = ar.astype(float)
print(ar.dtype)
print(ar)
print()

### 12 ### 

ar = np.linspace(0,10,50)
print(ar)
ar = np.arange(0,10.1,0.2)
print(ar)

### 13 ###
ar1 = np.arange(1,6)
ar2 = np.arange(1,6)

ar1 = np.sqrt(ar1)
ar_result = ar1 - ar2
print(ar1)
print(ar2)
print(ar_result)
print()

### 14 ###
ar = np.random.randint(0,100,15)
print(ar)
mar = ma.masked_array(ar, mask=[ar%2 == 0])
mar = ma.masked_array(ar, mask=[ar%2 != 0], fill_value=-1)
print(mar.filled())