import numpy as np
myArray = np.array([1,3,4,5,6,7,8])

def MaxProduct(array):
    MaxProduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] * array[j] > MaxProduct:
                MaxProduct = array[i] * array[j]
                pair = str(array[i]) +" , " + str(array[j])
    print(pair) 
    print(MaxProduct)  
    
MaxProduct(myArray)             