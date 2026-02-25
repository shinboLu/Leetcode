class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(nrow):
            for j in range(i+1, ncol):
                print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(nrow):
            matrix[i].reverse()
