class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0 
        for i in range(len(s)):
            mapping = collections.defaultdict(int)
            for j in range(i, len(s)):
                mapping[s[j]] +=1
                if len(set(list(mapping.values()))) == 1:
                    res = max(res, j - i +1)

        return res