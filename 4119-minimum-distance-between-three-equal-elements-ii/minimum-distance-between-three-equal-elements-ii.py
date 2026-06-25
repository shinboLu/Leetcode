class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        visited = collections.defaultdict(list)
        res = float('inf')
        for i in range(n):
            visited[nums[i]].append(i)

        for _, values in visited.items():
            if len(values) >= 3: 
                for i in range(len(values) - 2):
                    a, b, c = values[i], values[i+1], values[i+2]
                    res = min(res, abs(a-b) + abs(b-c) + abs(c-a))

        return res if res != float('inf') else -1