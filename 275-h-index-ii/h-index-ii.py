class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, len(citations)-1

        while left <= right:
            mid = (left+right)
            if citations[mid] == n-mid:
                return n-mid
            elif citations[mid] < n-mid:
                left = mid+1
            else:
                right = mid-1

        return n-left
