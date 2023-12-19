class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0

        def backtrack(index, combs):
            nonlocal res 
            if len(combs) != len(set(combs)):
                return

            res = max(res, len(combs))

            for i in range(index, len(arr)):
                backtrack(i+1, combs+arr[i])
 
        backtrack(0, '')
        return res 
