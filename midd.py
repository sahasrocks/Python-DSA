def middle(lst):
    new = lst[1:]  
    del new[-1]
    return new

myList = [1,2,3,4]
print(middle(myList))