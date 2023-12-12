class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        ## store all possible and correct combination 
        def bt_update_res(index, path):
          
            if index == n + 1:
                if len(path) == k:
                    res.append(path.copy())
                return 
            if len(path) == k:
               
                res.append(path.copy())
             
                return 

 
            for i in range(index, n+1):
                path.append(i)
                bt_update_res(i + 1, path)
          
                path.pop()

        bt_update_res(1, [])


        return res 
                
            