class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if len(set(wordsDict)) == 1:
            return 1

        pos1, pos2 = [], []
        min_dist = float('inf')

        for idx, val in enumerate(wordsDict):
            if val == word1:
                pos1.append(idx) 
            if val == word2:
                pos2.append(idx)

        ## case equal
        print(pos1)
        if word1 == word2:
            for i in range(1, len(pos1)):
                min_dist = min(min_dist, abs(pos1[i] - pos1[i-1]))
            return min_dist 
        

        ## case unequal 
        l1, l2 = 0, 0

        min_diff = float('inf')

        while l1 < len(pos1) and l2 < len(pos2):
            min_diff = min(min_diff, abs(pos1[l1] - pos2[l2]))
            if pos1[l1] < pos2[l2]:
                l1 += 1
            else:
                l2 +=1
        return min_diff