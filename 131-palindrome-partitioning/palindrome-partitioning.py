class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        def backtrack(index, combs):
            if index == len(s):
                res.append(combs.copy())
                return 
            
            for i in range(index, len(s)):
                next_str = s[index:i+1]
                if next_str == next_str[::-1]:
                    combs.append(next_str)
                    backtrack(i+1,combs)
                    combs.pop()

        backtrack(0, [])
        return res