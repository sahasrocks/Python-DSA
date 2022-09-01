def finndPair(num,tar):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i]==num[j]:
                continue
            elif num[i] + num[j] == tar:
                print(i,j)
                
list = [1,2,3,4,5,6]
finndPair(list,4)
                