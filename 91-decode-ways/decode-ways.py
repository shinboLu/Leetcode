from string import ascii_uppercase
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=2000)
        def backtracking(index):
            if index == len(s):
                return 1
            
            if s[index] == '0':
                return 0

            if index == len(s)-1:
                return 1
            
            res = backtracking(index+1)

            if int(s[index:index+2]) <= 26:
                res += backtracking(index+2)

            return res


        return backtracking(0)
            


            
            


        backtracking(1,[])
        print(res)
        return len(res)






        