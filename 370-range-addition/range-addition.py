class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        a = [0] * (length + 1)
        for s, e, v in updates:
            a[s] += v
            a[e + 1] -= v
        ans = [0] * length
        cur = 0
        for i in range(length):
            cur += a[i]
            ans[i] = cur
        return ans
        