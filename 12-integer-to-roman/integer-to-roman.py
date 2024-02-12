class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }

        values = sorted(list(num_map.keys()), reverse=True)

        res = ''

        for val in values:
            while val <= num:
                res += num_map[val]
                num -= val
        return res
