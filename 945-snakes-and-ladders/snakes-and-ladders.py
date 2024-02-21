class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        graph = [None] * (n**2+1)
        label = 1
        columns = list(range(0, n)) 

        for row in range(n-1, -1, -1):
            for col in columns:
                graph[label] = [row, col]
                label += 1
            columns.reverse() 

        dist = [-1] * (n ** 2 +1)

        queue = collections.deque([1])
        dist[1] = 0 
        while queue:
            cur = queue.popleft() 
            for nxt in range(cur+1, min(cur+6, n ** 2)+1):
                row, col = graph[nxt]
                destination = board[row][col] if board[row][col] != -1 else nxt

                if dist[destination] == -1:
                    dist[destination] = dist[cur] + 1
                    queue.append(destination)
        return dist[n*n]