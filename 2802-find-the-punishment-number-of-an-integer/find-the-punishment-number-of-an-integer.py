class Solution:
    def punishmentNumber(self, n: int) -> int:

        def bt_check_is_punishNumber(idx, p, target):
            if idx == len(p):
                return target == 0
            if target < 0:
                return False

            for i in range(idx, len(p)):
                x = p[idx:i + 1]
                y = int(x)
                if bt_check_is_punishNumber(i+1, p, target-y):
                    return True
            return False

        res = 0
        for i in range(1, n+1):
            x = i * i
            number = str(x)

            if bt_check_is_punishNumber(0, number, i):
                res += x
        return res
        

                

