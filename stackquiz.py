#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    #  Push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    # Pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]

    #  delete
    def delete(self):
        self.list = None

m = Stack(5)
m.push('x')
m.push('y')
m.pop()
m.push('z')
m.peek()




