class TrieNode:
    def __init__(self):
        self.children = {}
        self.tot_sum = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        for ch in key:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch] 
            cur.tot_sum += diff


    def sum(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch] 
        return cur.tot_sum 

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)