class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursion(start, end, ls):
            if start >= end:
                return

            ls[start], ls[end] = ls[end], ls[start]

            return recursion(start+1, end-1, ls)

        recursion(0, len(s)-1, s)