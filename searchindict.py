myDict = {'name': 'op', 'age':'23' , 'address':'pakistan'}

def search(dict,value):
    for key in dict:
        if dict[key]== value:
            return key,value
        
    return 'The vvalue is not Found'
print(search(myDict,'23'))    