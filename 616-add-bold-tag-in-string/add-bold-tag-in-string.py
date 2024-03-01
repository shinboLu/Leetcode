class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_end = True 

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w) 
        pairs = [] 
        for i in range(len(s)):
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.is_end:
                    pairs.append([i, j])

        if not pairs:
            return s

        start, end = pairs[0]
        breaks = [] 
        for n_start, n_end in pairs[1:]:
            if end + 1 < n_start:
                breaks.append([start, end])
                start, end = n_start, n_end 
            else: 
                end = max(end, n_end)

        breaks.append([start, end])

        ans = []
        i = j = 0
        while i < len(s):
            if j == len(breaks):
                ans.append(s[i:])
                break
            st, ed = breaks[j]
            if i < st:
                ans.append(s[i:st])
            ans.append('<b>')
            ans.append(s[st : ed + 1])
            ans.append('</b>')
            j += 1
            i = ed + 1

        return ''.join(ans)

         