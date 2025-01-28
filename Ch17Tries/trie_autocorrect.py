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
    
    def collectAllWords(self,node=None,word="",words=[]):
        currentNode=node or self.root
        
        for key, childNode in currentNode.children.items():
            if key=="*":
                words.append(word)
            else:
                self.collectAllWords(childNode,word+key,words)
        
        return words   
    


        