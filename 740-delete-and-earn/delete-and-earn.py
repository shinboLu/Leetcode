class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = collections.defaultdict(int) 

        max_num = 0

        for num in nums:
            points[num] += num 
            max_num = max(max_num, num) 

        #print(points, max_num)

        dp = [0] * (max_num+1)
        dp[1] = points[1]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])

        return dp[max_num]