class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for start, dest in sorted(tickets, reverse=True):

            graph[start].append(dest)

        res = []


        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())

            res.append(airport)

        dfs("JFK")
        return res[::-1]
        
            