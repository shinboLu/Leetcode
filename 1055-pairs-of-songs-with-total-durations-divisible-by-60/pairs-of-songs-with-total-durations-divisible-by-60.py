class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = collections.defaultdict(int)
        res = 0

        for t in time:
            if t % 60 == 0:
                res += remainder[0]

            else:
                res += remainder[60 - t % 60]

            remainder[t % 60] += 1

        return res

        