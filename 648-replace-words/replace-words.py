class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root 
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch] 
        cur.end_word = True 

class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_map = Trie()
        for word in dictionary:
            word_map.insert(word)

        words = sentence.split(' ')
        res = [] 
        for w in words:
            cur = word_map.root 
            temp = '' 
            exist = False

            for ch in w: 
                if cur.end_word:
                    exist = True 
                    break 
                if ch in cur.children:
                    temp += ch
                    cur = cur.children[ch] 
                else:
                    break 

            if cur.end_word:
                exist = True 
            
            if not temp or not exist:
                res.append(w)

            elif temp and exist:
                res.append(temp) 

        return ' '.join(res)

              

        
        