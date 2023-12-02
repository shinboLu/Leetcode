class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = collections.defaultdict(int)

        def backtracking_return_count(idx, total):
            nonlocal dic
            key = (idx, total)

            if key not in dic:
                if idx == len(nums):
                    return 1 if total == target else 0

                else:
                    dic[key] = backtracking_return_count(idx + 1, total + nums[idx]) + backtracking_return_count(idx+1, total - nums[idx])

            return dic[key]

        return backtracking_return_count(0, 0)
