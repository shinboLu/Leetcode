class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.hash_map.keys():
            return False
        self.hash_map[val] = len(self.list)
        self.list.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val in self.hash_map.keys():
            last_el, idx = self.list[-1], self.hash_map[val]
            self.list[idx], self.hash_map[last_el] = last_el, idx
            self.list.pop()
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