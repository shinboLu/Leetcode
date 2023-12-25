class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def backtrack(index):
            if index > n:
                return

            res.append(index)

            for i in range(0, 10):
                backtrack(index * 10 + i)


        for i in range(1, 10):
            backtrack(i) 

        return res 