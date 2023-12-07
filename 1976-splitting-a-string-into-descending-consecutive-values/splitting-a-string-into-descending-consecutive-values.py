class Solution:
    def splitString(self, s: str) -> bool:
        res = []
        def backtracking_return_boolean(index, prev):
            if index == len(s):
                return True

            for i in range(index, len(s)):
                val = int(s[index:i+1])
                if val + 1 == prev and backtracking_return_boolean(i+1, val):
                    return True
            return False

        for i in range(len(s)-1):
            val = int(s[:i+1])
            if backtracking_return_boolean(i+1, val):
                return True
        
        return False

