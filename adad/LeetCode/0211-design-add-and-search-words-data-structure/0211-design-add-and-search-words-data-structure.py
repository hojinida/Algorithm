class Node:
     def __init__(self):
        self.childNode = {} 
        self.end = False 

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.childNode:
                node.childNode[char] = Node()
            node = node.childNode[char]
        node.end = True

        pass

    def search(self, word: str) -> bool:
        def deepSearch(node, word):
            for i in range(len(word)):
                char = word[i]
                if char == ".":
                    for child in node.childNode.values():
                        if deepSearch(child, word[i + 1:]): 
                            return True
                    return False
                if char not in node.childNode:  
                    return False
                node = node.childNode[char]  
            return node.end  

        return deepSearch(self.root, word) 
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)