class Node:
    def __init__(self):
        self.children = {}  
        self.is_end = False 

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = Node()
            node = node.children[s]

        node.is_end = True
    
        pass

    def search(self, word: str) -> bool:
        node = self.root
        for s in word:
            if s not in node.children:
                return False
            node = node.children[s]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for s in prefix:
            if s not in node.children:
                return False
            node = node.children[s]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)