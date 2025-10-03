class RandomizedSet:

    def __init__(self):
        self.val_list = []
        self.val_mapping = {}


    def insert(self, val: int) -> bool:
        if val not in self.val_list:
            self.val_list.append(val)
            self.val_mapping[val] = len(self.val_list)-1
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.val_list:
            target_idx = self.val_mapping[val]
            last_el = self.val_list[-1]
            self.val_list[-1], self.val_list[target_idx] = self.val_list[target_idx], self.val_list[-1]
            self.val_mapping[last_el] = target_idx
            del self.val_mapping[val]
            self.val_list.pop() 
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.val_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()