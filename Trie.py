class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insertString(self,word):
        current = self.root
        for i in word:
            ch = 1
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node}) 
            current = node
        current.endOfString = True
        print("Succesfully inserted")           
    
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False  
    
    
    
    
        
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
#deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))