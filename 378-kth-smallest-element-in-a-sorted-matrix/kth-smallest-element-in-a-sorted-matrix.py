from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        min_heap = [] 
        for i in range(min(k, n)):
            min_heap.append((matrix[i][0], i, 0))

        heapify(min_heap)

        while k:
            first_val_row, row_idx, col_idx = heappop(min_heap)

            if col_idx < n -1:
                heappush(min_heap, (matrix[row_idx][col_idx+1], row_idx, col_idx+1))
            k-=1
        return first_val_row
