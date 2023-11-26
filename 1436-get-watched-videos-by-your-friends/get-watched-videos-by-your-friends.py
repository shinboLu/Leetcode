class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = collections.defaultdict(int)
        queue = collections.deque()
        queue.append([id , 0])
        visited = [0] * len(friends)
        visited[id] = 1

        while queue:
            curr_pos, dist = queue.popleft()
            for next_pos in friends[curr_pos]:
                if visited[next_pos] == 0 and dist + 1 <= level:
                    if dist + 1 == level:
                        for j in watchedVideos[next_pos]:
                            graph[j] += 1 
                    queue.append((next_pos, dist + 1))
                    visited[next_pos] = 1

        res = sorted(graph, key = lambda x : (graph[x], x))

        return res
