class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.map = collections.defaultdict(set)

        for word in dictionary:
            if len(word) >= 3:
                abbr = word[0] + str(len(word)-2) + word[-1]
                self.map[abbr].add(word)
            else:
                self.map[word].add(word)
        #print(self.map)

    def isUnique(self, word: str) -> bool:

        if len(word) >= 3:
            abbr = word[0] + str(len(word)-2) + word[-1]
        else:
            abbr = word

        
        if abbr not in self.map or (abbr in self.map and len(self.map[abbr]) == 1 and word in self.map[abbr]) :
            return True 
        
        # if abbr in self.map and word in self.map[abbr]:
        #     return True 
        print(abbr,  self.map[abbr])
        return False

        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)