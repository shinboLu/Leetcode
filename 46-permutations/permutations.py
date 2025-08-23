class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = [] 
        self.visited = [False] * len(nums) 
        def bt(nums,cur):
            if len(cur) == len(nums):
                self.res.append(cur.copy())
                return 
            for i in range(len(nums)):
                if self.visited[i]:
                    continue
                cur.append(nums[i])
                self.visited[i] = True
                bt(nums, cur)
                cur.pop()
                self.visited[i] = False

        bt(nums, [])
        return self.res