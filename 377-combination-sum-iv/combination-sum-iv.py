class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @functools.lru_cache(maxsize = None)
        def combs(remain):
            if remain == 0:
                return 1

            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combs(remain - num)

            return result

        return combs(target)