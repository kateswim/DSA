patterns = ['this', 'that', 'here', 'there']

class TrieNode():
    def __init__(self):
        self.childern={}

class Trie:
    def __init__(self):
        self.root = TrieNode()

def trie_construction(patterns = patterns):
    trie = Trie() # this contains root only.

    for pattern in patterns:
        print(pattern)
        currentNode = trie.root
        print(currentNode)
        print(currentNode.childern)

        for alphabet in pattern:
            currentSymbol = alphabet
            if currentSymbol in currentNode.childern :
                currentNode = currentNode.childern[currentSymbol]
            else:
                new_node = TrieNode()
                currentNode.childern[currentSymbol] = new_node
                currentNode = new_node
                pass

    return trie

trie = trie_construction(patterns = patterns)
