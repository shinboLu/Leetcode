class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_list = []
        #self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch] 
            if len(cur.word_list) < 3:
                cur.word_list.append(word)

        #cur.is_end = True

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() 
        trie = Trie()
        for word in products:
            trie.insert(word) 
        cur = trie.root 

        res = [[] for _ in range(len(searchWord))]

        for i in range(len(searchWord)):
            if searchWord[i] not in cur.children:
                break
            cur = cur.children[searchWord[i]]
            res[i] = cur.word_list

        return res 

             