from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIR = [[0, 1], [1, 0], [-1, 0], [0,-1]]
        nrow = len(heights)
        ncol = len(heights[0])

        difference_matrix = [[float('inf')] * ncol for _ in range(nrow)]
        difference_matrix[0][0] = 0

        visited = [[False] * ncol for _ in range(nrow)]
        min_heap = [(0, 0, 0)] ## (difference, x, y)

        while min_heap:
            difference, x, y = heappop(min_heap)
            visited[x][y] = True

            for dx, dy in DIR:
                adj_x, adj_y = x + dx, y + dy

                if 0 <= adj_x < nrow and 0 <= adj_y < ncol and not visited[adj_x][adj_y]:
                    curr_difference = abs(heights[adj_x][adj_y] - heights[x][y])
                    max_difference = max(curr_difference, difference_matrix[x][y])
                    if difference_matrix[adj_x][adj_y] > max_difference:
                        difference_matrix[adj_x][adj_y] = max_difference
                        heappush(min_heap, (max_difference, adj_x, adj_y))
        return difference_matrix[-1][-1]