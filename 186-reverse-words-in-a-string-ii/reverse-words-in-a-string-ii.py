class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self.reverse(0, len(s)-1, s)
        self.reverse_word(s)

    def reverse(self, left, right, li):
        while left < right:
            li[left], li[right] = li[right], li[left]
            left, right = left+1, right-1

    def reverse_word(self, li):
        n = len(li)
        start = end = 0

        while start < n:
            while end < n and li[end] != ' ':
                end += 1

            self.reverse(start, end-1, li)
            start = end + 1
            end += 1


    

        