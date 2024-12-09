class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','')
        left = 0
        right = len(s)-1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()
            if left_char.isalnum() and right_char.isalnum():
                if left_char == right_char:
                    left+=1
                    right-=1
                    continue
                else:
                    return False
            elif not left_char.isalnum() and right_char.isalnum():
                left+=1
            elif not left_char.isalnum() and not right_char.isalnum():
                left+=1
                right-=1
            else:
                right-=1
            

        return True