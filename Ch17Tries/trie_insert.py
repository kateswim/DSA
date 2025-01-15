class TrieNode():
    def __init__(self):
        self.children={}

class Trie():
    def __init__(self):
        self.root=TrieNode()

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


    def collectAllWords(self,node=None,word="",words=[]):
        currentNode=node or self.root
        
        for key, childNode in currentNode.children.items():
            if key=="*":
                words.append(word)
            else:
                self.collectAllWords(childNode,word+key,words)
        
        return words
                  

trie = Trie()

trie.insert("cat")
trie.insert("car")
trie.insert("cart")

print(trie.collectAllWords())