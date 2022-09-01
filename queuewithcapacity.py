class Queue:
    def __init__(self,maxSize):
        self.items = maxSize *[None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values) 
    
    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False
        
        
    def enqueue(self,value):
        if self.isFull():
            return "The queue is full."
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element ius inserted at end"                
        
customQueue = Queue(2)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
       
           