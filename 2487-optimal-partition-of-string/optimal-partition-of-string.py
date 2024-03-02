class Solution:
    def partitionString(self, s: str) -> int:
        visited = set() 
        count = 0 

        for ch in s: 
            if ch in visited:
                count += 1
                visited = set(ch) 
            else:
                visited.add(ch)

        return count + 1
