class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_dict = collections.Counter(s1)
        visited = collections.Counter(s2[:len(s1)])
        if target_dict == visited:
            return True

        for i in range(len(s1), len(s2)): 
            visited[s2[i]] += 1
            visited[s2[i-len(s1)]] -=1
            if visited[s2[i-len(s1)]] == 0:
                del visited[i-len(s1)]
            
            if visited == target_dict: 
                return True

        return False

            