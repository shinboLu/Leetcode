class Solution:
    def reverse(self, x: int) -> int:
        _range = range(-2**31, 2**31-1)
        is_neg = False
        res = 0
        if x < 0:
            is_neg = True

        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x //10 
            res = res * 10 + digit

        if is_neg and res in _range: 
            return -res
        elif not is_neg and res in _range:
            return res
        else:
            return 0