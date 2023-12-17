class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n+1)

        res = 0

        def bt(combs):
            nonlocal res 
            if len(combs) == n:
                res += 1
                return 

            for num in range(1, n+1):
                index = len(combs) + 1 
                if not visited[num] and (num % index == 0 or index % num == 0):
                    combs.append(num)
                    visited[num] = True
                    bt(combs)
                    combs.pop()
                    visited[num] = False

        bt([])
        return res 

                
        


