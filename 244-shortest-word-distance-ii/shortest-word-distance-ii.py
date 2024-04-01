class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = collections.defaultdict(list)
        for idx, val in enumerate(wordsDict):
            self.dict[val].append(idx)
        

    def shortest(self, word1: str, word2: str) -> int:
        pos1 = self.dict[word1]
        pos2 = self.dict[word2]
        l1, l2 = 0, 0

        min_diff = float('inf')

        while l1 < len(pos1) and l2 < len(pos2):
            min_diff = min(min_diff, abs(pos1[l1] - pos2[l2]))
            if pos1[l1] < pos2[l2]:
                l1 += 1
            else:
                l2 +=1
        return min_diff
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)