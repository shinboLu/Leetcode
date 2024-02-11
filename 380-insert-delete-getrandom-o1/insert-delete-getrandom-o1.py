class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        
    def insert(self, val: int) -> bool:
        if val in self.hash_map.keys():
            return False
        self.hash_map[val] = 0
        return True
    
    def remove(self, val: int) -> bool:
        if val in self.hash_map.keys():
            del self.hash_map[val]
            return True
        return False
    def getRandom(self) -> int:
        li = list(self.hash_map.keys())
        return random.choice(li)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()