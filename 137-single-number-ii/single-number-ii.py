class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}

        for num in nums: 
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for k in freq.keys():
            if freq[k] == 1:
                return k