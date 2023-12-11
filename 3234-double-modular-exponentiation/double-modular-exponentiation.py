class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = [] 
        for idx, var in enumerate(variables):
            if ((var[0] ** var[1] % 10) ** var[2]) % var[3] == target:
                res.append(idx)

        return res
                
            