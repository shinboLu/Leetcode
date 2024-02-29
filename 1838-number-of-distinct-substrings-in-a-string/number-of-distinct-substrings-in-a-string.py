class Trie:
    def __init__(self):
        self.children = [None] * 26

class Solution:
    def countDistinct(self, s: str) -> int:
        root = Trie()
        count = 0

        for i in range(len(s)):
            current = root
            for j in range(i, len(s)):
                index = ord(s[j]) - ord('a')

                if current.children[index] is None:
                    current.children[index] = Trie()
                    count += 1

                current = current.children[index]

        return count