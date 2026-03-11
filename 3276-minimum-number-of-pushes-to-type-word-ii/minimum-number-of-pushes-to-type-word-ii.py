class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26 
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            freq[idx] +=1

        freq.sort(reverse=True) 
        print(freq)
        res = 0
        for idx, val in enumerate(freq):
            if val == 0:
                break
            res += (idx//8+1) * val
        return res
