class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.split(' ')
        res = []

        for el in li:
            if el:
                res.append(el)

        return len(res[-1])
