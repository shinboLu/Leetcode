class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'a', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        st = [i for i in s]
        left, right = 0, len(st)-1

        while left < right:
            print(left, right, st[left], st[right])
            if st[left] in vowels and st[right] in vowels:
                print('here')
                st[left], st[right] = st[right], st[left] 
                left += 1
                right -= 1
            elif st[left] in vowels and st[right] not in vowels:
                right -= 1
            elif st[left] not in vowels and st[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1


        return ''.join(st)