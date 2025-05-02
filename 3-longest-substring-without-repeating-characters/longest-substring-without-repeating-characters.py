class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=right=0
        mapping = {} 
        res = 0 

        while right < len(s):
            cur_char = s[right]
            right += 1
            mapping[cur_char] = mapping.get(cur_char,0)+1

            while mapping.get(cur_char) > 1:
                mapping[s[left]] = mapping.get(s[left])-1
                left +=1
            res = max(res, right-left)
        return res


