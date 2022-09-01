import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
newBT = TreeNode("Drinks")        
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild=tea
leftChild.rightChild=coffee
rightChild = TreeNode("Cold")
pespi = TreeNode("Pespi")
fanta = TreeNode("Fanta")
rightChild.rightChild=fanta
rightChild.leftChild=pespi
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
#preOrderTraversal(newBT)    

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
#inOrderTraversal(newBT)    

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

#postOrderTraversal(newBT)    

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)    
#levelOrderTraversal(newBT)                

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return "Not present"
    else:
        customQueue= queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "present"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
                
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not FOund"            
    
#print(searchBT(newBT,"Tea"))    

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)    
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Succesfully inserted"    
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Succesfully inserted"    

#newNode = TreeNode("Cola")
#print(insertNodeBT(newBT,newNode))
#levelOrderTraversal(newBT)            

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild) 
        deepestNode = root.value
        return deepestNode


#deepestNode = getDeepestNode(newBT)
#print(deepestNode.data)            


 

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

#levelOrderTraversal(newBT)            
#newNode = getDeepestNode(newBT)                   
#deleteDeepestNode(newBT,newNode)
#levelOrderTraversal(newBT)



def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "THe BT dont exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data ==node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "The Node is Deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "failed to delete"        
                    
#deleteNodeBT(newBT,'Pespi') 
#levelOrderTraversal(newBT)                   

def deleteBT(rootNode):
    rootNode.data =None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "The Bt is deleted"

#deleteBT(newBT)
#levelOrderTraversal(newBT)