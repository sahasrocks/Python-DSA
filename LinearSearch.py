def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linearSearch([1,2,3,40],3))    