class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_dict = collections.Counter(s1)
        visited = collections.defaultdict(int)
        left = 0 

        for right in range(len(s2)):
            visited[s2[right]] +=1

            if right - left +1 > len(s1):
                visited[s2[left]] -=1
                if visited[s2[left]] == 0:
                    del visited[s2[left]]
                left +=1
            
            if visited == target_dict:
                return True
        return False
            
