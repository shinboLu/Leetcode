class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def buildTree(dictionary):
            root = TrieNode()

            for word in dictionary:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char] 
                node.is_word = True
            return root

        root = buildTree(dictionary)
        n = len(s) 

        @cache
        def dp(idx):
            if idx == n:
                return 0
            nonlocal root 
            cur = root
            res = dp(idx+1) + 1
            
            for end in range(idx, n):
                if s[end] not in cur.children:
                    break  
                cur = cur.children[s[end]]
                if cur.is_word:
                    res = min(res, dp(end+1))
            return res 


        return dp(0)