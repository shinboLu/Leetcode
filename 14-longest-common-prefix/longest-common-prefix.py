class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch] 
        cur.is_end = True

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return '' 

        trie = Trie()

        for word in strs:
            trie.insert(word)

        cur = trie.root

        res = ''

        while cur:
            if len(cur.children) > 1 or cur.is_end:
                return res 

            key = list(cur.children)[0] 
            res += key 

            cur = cur.children[key]

        return res 

            

        return ''

        


        

        

