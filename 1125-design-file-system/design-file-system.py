class Trie:
    def __init__(self, val:int = -1):
        self.children = {}
        self.val = val

    def insert(self, path, val):
        root = self 
        paths = path.split('/')
        for p in paths[1:-1]:
            if p not in root.children:
                return False 
            root = root.children[p] 
        
        if paths[-1] in root.children:
            return False

        root.children[paths[-1]] = Trie(val) 
        return True 
    
    def search(self, path):
        root = self 
        for p in path.split('/')[1:]:
            if p not in root.children:
                return -1
            root = root.children[p] 
        return root.val

class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.trie.insert(path, value)

    def get(self, path: str) -> int:
        return self.trie.search(path)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)