from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        counter = Counter(nums)

        for k, v in counter.items():
            if v >= 2:
                return True

        return False 

