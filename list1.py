myList=list()
while (True):
    inp = input('Enter a No')
    if inp =='done': break
    value = float(inp)
    myList.append(value)
average =sum(myList)/len(myList)

print('average:',average)