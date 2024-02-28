class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if cur.children.get(idx, -1) == -1:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if cur.children.get(idx, -1) == -1:
                return False 
            cur = cur.children[idx]
        if cur.is_end == True:
            return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if cur.children.get(idx, -1) == -1:
                return False

            cur = cur.children[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)