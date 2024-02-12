class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''

        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                st += s[i].lower()
        print(st)
        return st == st[::-1]