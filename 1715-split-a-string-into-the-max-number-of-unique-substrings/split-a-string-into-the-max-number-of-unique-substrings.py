class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtracking(start_index, used):
            if start_index == len(s):
                return len(used)

            curr = ''
            ans = 0

            for i in range(start_index, len(s)):
                curr = curr + s[i]
                if curr in used:
                    continue

                used.add(curr)
                ans = max(ans, backtracking(i+1, used))
                used.remove(curr)
            
            return ans
        
        return backtracking(0,set())


            

            
