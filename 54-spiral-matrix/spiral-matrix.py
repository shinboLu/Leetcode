class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] 

        m, n = len(matrix), len(matrix[0])
        upper_bound, lower_bound = 0, m-1
        left_bound, right_bound = 0, n-1

        # m=3, upper_bound = 0, lower_bound = 2
        # n = 4, left_bound = 0, right_bound = 3

        while len(res) < m*n:
            if upper_bound <= lower_bound:
                for i in range(left_bound, right_bound+1):
                    res.append(matrix[upper_bound][i]) 
                upper_bound+=1
            
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound+1):
                    res.append(matrix[i][right_bound])
                right_bound -=1 

            if upper_bound <= lower_bound:
                for i in range(right_bound, left_bound-1, -1):
                    res.append(matrix[lower_bound][i]) 
                lower_bound -=1 
            
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound-1, -1):
                    res.append(matrix[i][left_bound])
                left_bound+=1
        
        return res
            


