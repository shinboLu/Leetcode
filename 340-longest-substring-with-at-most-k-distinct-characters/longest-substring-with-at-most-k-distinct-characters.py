class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0 
        right = 0 
        counter = collections.Counter()
        res = 0
        while right < len(s):
            counter[s[right]] += 1
            right+=1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]] 
                left += 1
            res = max(res, right-left+1)
        return res-1
