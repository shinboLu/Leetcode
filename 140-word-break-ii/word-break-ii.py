class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def backtracking(index, combs):
            if index == len(s):
                res.append(' '.join(combs))
                return 

            for i in range(index, len(s)):
                cur = s[index:i+1]
                if cur in wordDict:
                    combs.append(cur)
                    backtracking(i+1, combs)
                    combs.pop()

        backtracking(0,[])
        return res 