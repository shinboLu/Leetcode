class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        visited = set() 
        while nums:
            cur = nums.pop()
            if cur in nums or cur in visited:
                visited.add(cur) 
            else:
                yield cur
