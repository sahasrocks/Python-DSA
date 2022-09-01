myList = [1,3,4,5,6,7,8]

def searchInList(list, value ):
    for i in list:
        if i ==value:
            return list.index(value)
    return 'The value not exist in the list'
print(searchInList(myList,23))            