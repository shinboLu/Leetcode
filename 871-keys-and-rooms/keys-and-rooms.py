class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True 

        stack = [0]

        while stack:
            node = stack.pop(0)

            for nei in rooms[node]:
                if not visited[nei]:
                    visited[nei] = True 
                    stack.append(nei) 

        return all(visited)

            

