class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []

        def backtrack(index, combs):
            if index == len(s):
                res.append(' '.join(combs))
                return

            for i in range(index, len(s)):
                cur_word = s[index:i+1]
                if cur_word in wordDict:
                    combs.append(cur_word)
                    backtrack(i+1, combs)
                    combs.pop()

        backtrack(0, [])
        return res 

