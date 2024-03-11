class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
        if not heights or not heights[0]:
            return [] 

        nrow = len(heights)
        ncol = len(heights[0])

        pacific_queue = collections.deque() 
        atlantic_queue = collections.deque() 

        for i in range(nrow):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, ncol-1))

        for i in range(ncol):
            pacific_queue.append((0, i)) 
            atlantic_queue.append((nrow-1, i)) 


        def bfs(queue): 
            reachable = set()

            while queue:
                row, col = queue.popleft()
                reachable.add((row, col)) 
                for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = row + x, y + col
                    if nx < 0 or nx >= nrow or ny < 0 or ny >= ncol:
                        continue 
                    if (nx, ny) in reachable:
                        continue 
                    if heights[nx][ny] < heights[row][col]:
                        continue 

                    queue.append((nx, ny)) 

            return reachable 

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue) 

        return list(pacific_reachable.intersection(atlantic_reachable))