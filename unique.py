myList = [1,2,3,4,5,6,8,9,78,2,53]

def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True
    
print(isUnique(myList))        