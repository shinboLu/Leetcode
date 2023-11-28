class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        print(len(rooms))
        graph = collections.defaultdict(list)
        indegree = [0] * len(rooms)
        for idx, val in enumerate(rooms):
            for element in val:
                graph[idx].append(element)

        queue = collections.deque()
        queue.append(0)
        visited = set()
        unlocked_room = 0 
        

        while queue:
            #print(queue)
            cur_room = queue.popleft()
            for next_room in graph[cur_room]:
                if next_room not in visited and cur_room != next_room or not next_room: 
                    queue.append(next_room)
                    visited.add(next_room)
                    unlocked_room +=1
                    print(unlocked_room)

        return True if unlocked_room == len(rooms)-1 else False

