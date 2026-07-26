class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[:k])
        right_sum = 0

        res = left_sum
        for i in range(k):
            left_sum -= cardPoints[k-1-i]
            right_sum += cardPoints[len(cardPoints) - i - 1]
            res = max(res, left_sum + right_sum)

        return res