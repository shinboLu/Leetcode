class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        length = math.ceil(intLength/2)
        res = []

        odd = intLength % 2 == 1

        base = 10 ** (length-1)

        def getPalindrome(query):
            val = str(query-1+base)
            if len(val) > length:
                return -1
            
            if odd:
                return int(val + val[-2::-1])

            else:
                return int(val + val[::-1])

        for query in queries:
            res.append(getPalindrome(query))

        return res 



