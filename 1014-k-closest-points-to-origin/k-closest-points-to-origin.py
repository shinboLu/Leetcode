class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = sorted(points, key=lambda p: p[0]**2 + p[1]**2)
        return res[:k]