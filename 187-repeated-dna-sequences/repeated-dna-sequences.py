class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        left = 10
        n = len(s)
        visited = set()
        res = set() 
        for i in range(n-left+1):
            cur = s[i:i+left]
            if cur in visited:
                res.add(cur[:])
            visited.add(cur)

        return res 

