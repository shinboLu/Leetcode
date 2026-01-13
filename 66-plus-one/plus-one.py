class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = digits[0]
        res = []
        for i in range(1,len(digits)):
            val = val * 10 + digits[i]

        val +=1

        for l in str(val): 
            res.append(int(l))

        return res