class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        res = []

        for i in range(len(temp)-1, -1, -1):
            res.append(temp[i])

        return ' '.join(res)
