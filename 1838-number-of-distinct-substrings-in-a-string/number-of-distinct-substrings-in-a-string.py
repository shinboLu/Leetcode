class Trie:
    def __init__(self):
        self.children = {}

class Solution:
    def countDistinct(self, s: str) -> int:
        root = Trie()
        count = 0

        for i in range(len(s)):
            current = root
            for j in range(i, len(s)):
                ch = s[j]

                if ch not in current.children:
                    current.children[ch] = Trie()
                    count += 1

                current = current.children[ch]

        return count