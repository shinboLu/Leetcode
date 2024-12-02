class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}

        for char in t:
            need[char] = need.get(char,0) + 1 
        
        left = right = valid = 0 
        start = 0 
        length = float('inf')

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right-left < length:
                    start = left
                    length = right-left
                d = s[left] 
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return '' if length == float('inf') else s[start:start+length]