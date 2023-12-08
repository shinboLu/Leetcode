class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def recursion(start, end):
            if start < end:
                s[start], s[end] = s[end], s[start]
                recursion(start+1, end-1)

        recursion(0, len(s)-1)