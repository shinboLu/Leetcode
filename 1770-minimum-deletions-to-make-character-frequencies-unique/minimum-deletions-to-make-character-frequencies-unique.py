class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = [0] * 26
        
        for ch in s:
            frequency[ord(ch) - ord('a')] += 1
        
        delete_count = 0

        visited = set() 

        for i in range(26):
            while frequency[i] and frequency[i] in visited:
                frequency[i] -= 1
                delete_count += 1

            visited.add(frequency[i]) 

        return delete_count
