from array import *
myarray = array('i',[1,2,3,4,5])
for i in myarray:
    print(i)
    

myarray.append(56)
print(myarray)    

myarray.insert(0,23)
print(myarray)
myarray.insert(4,423)
print(myarray)
myarray1 = array('i',[12,22,31,42,43])
myarray.extend(myarray1)
print(myarray)

myarray.remove(12)
print(myarray)

myarray.pop()
print(myarray)

myarray.reverse()
print(myarray)
myarray.reverse()
print(myarray)
print('opop')
#print(myarray.tolist())

print(myarray[1:6])