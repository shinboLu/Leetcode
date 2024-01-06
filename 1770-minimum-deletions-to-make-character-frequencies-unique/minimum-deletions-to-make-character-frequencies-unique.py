class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        freq = list(counter.values())
        delete_count = 0

        visited = set() 

        for i in range(len(freq)):
            while freq[i] and freq[i] in visited:
                freq[i] -= 1
                delete_count += 1

            visited.add(freq[i]) 

        return delete_count
