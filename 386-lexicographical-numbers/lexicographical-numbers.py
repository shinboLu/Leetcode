class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(index):
            if index > n:
                return 
            
            res.append(index)

            for i in range(0, 10):
                dfs(index * 10 + i)

        for i in range(1, 10):
            dfs(i)

        return res 