class TrieNode():
    def __init__(self):
        self.children={}

class Trie():
    def __init__(self):
        self.root=TrieNode()

    def search(self,word):
        currentNode=self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode=currentNode.children[char] #follow the child node

            else:
                return None
    
        return currentNode
    
    def insert(self,word):
        currentNode=self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode=currentNode.children[char] #follow the child node

            else:
            
                newNode=TrieNode()
                currentNode.children[char]=newNode

                currentNode=newNode #follow new node
    
        currentNode.children["*"]=None #after all word add * key at the end        



trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("cart")
trie.insert("dog")

# search for exact words
print(trie.search("cat"))  
print(trie.search("cart"))  
print(trie.search("cars"))   