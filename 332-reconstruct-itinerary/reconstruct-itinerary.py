class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        res = []

        def dfs(airport):
            while adj[airport]:
                # Always take the smallest lexicographic option
                next_airport = adj[airport].pop(0)
                dfs(next_airport)
            res.append(airport)

        dfs("JFK")
        return res[::-1]
            