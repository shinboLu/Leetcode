class Solution:
    def hIndex(self, c: List[int]) -> int:
        n = len(c) 
        c.sort() 
        for idx, val in enumerate(c):
            if n - idx <= val :
                return n - idx

        return 0