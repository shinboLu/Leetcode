class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])

        left = [0] * ncol
        right = [ncol] * ncol
        height = [0] * ncol

        maxarea = 0

        for i in range(nrow):
            cur_left, cur_right = 0, ncol
            for j in range(ncol):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(ncol):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            for j in range(ncol-1, -1, -1):
                if matrix[i][j] == '1': 
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = ncol
                    cur_right = j
            for j in range(ncol):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea
