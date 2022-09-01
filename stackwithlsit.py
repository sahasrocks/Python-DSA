class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]    
        return '\n'.join(values)
    
    # is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False


    #push 
    def push(self, value):
        self.list.append(value)
        return 'The element has been sussesfully aDDED'
    
    #pop 
    def pop(self):
        if self.isEmpty():
            return 'There is no element in the list'
        else:
            return self.list.pop()
     
     #peek return lastelement
    def peek(self):
        if self.isEmpty():
            return 'there is no element in the list'
        else:
            return self.list[len(self.list)-1]
                
        
        
customStack = Stack()
#print(customStack.isEmpty())        
customStack.push(1)
customStack.push(2)
customStack.push(3)
#print(customStack)
customStack.pop()
print(customStack)
print(customStack.peek())