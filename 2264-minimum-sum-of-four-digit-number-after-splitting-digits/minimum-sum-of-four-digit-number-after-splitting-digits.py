class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num), reverse=True )
        print(num)
        return int(num[0]) + int(num[1]) + int(num[2]) * 10 + int(num[3])*10
