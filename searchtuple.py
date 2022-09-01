newTuples = ('a', 'b', 'c')

def searchtuple(pTuple,element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'Not PResent'

print(searchtuple(newTuples,'c'))    