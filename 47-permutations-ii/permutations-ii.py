class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        visited = [False] * len(nums)
        res = []

        def bt(combs): 
            if len(combs) == len(nums):
                res.append(combs.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue 
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                combs.append(nums[i]) 
                #print(combs)
                bt(combs)
                combs.pop()
                visited[i] = False

        bt([])
        return res 