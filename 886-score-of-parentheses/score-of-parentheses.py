class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        def dfs(left, right):
            if right - left == 1:
                return 1
            
            count = 0
            for i in range(left ,right):
                if s[i] == '(':
                    count += 1
                
                if s[i] == ')':
                    count -= 1

                if count == 0:
                    return dfs(left, i) + dfs(i+1, right)

            return 2 * dfs(left +1, right - 1)

        return dfs(0, len(s) -1)