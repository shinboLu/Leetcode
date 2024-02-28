class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root 
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx] 
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        if node.is_end == True:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if node.children[idx] == None:
                return False
            node = node.children[idx] 

        return True 



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)