class RandomizedSet:

    def __init__(self):
        self.val_list = []
        self.mapping = {}

    def insert(self, val: int) -> bool:
        if val not in self.mapping.keys():
            self.mapping[val] = len(self.val_list)
            self.val_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.mapping:
            val_idx = self.mapping[val]
            last_val = self.val_list[-1]
            self.val_list[val_idx] = last_val
            self.val_list.pop()
            self.mapping[last_val] = val_idx
            del self.mapping[val] 
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.val_list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()