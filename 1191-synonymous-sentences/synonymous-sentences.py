class unionFind:
    def __init__(self, size) -> None:
        self.root = [x for x in range(size)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        ## building relations between synonyms
        uf = unionFind(len(synonyms) * 2 )
        cur_id, word_id_map, id_word_map = 0, collections.defaultdict(int), collections.defaultdict(str)

        for a, b in synonyms:
            if a not in word_id_map:
                word_id_map[a] = cur_id
                id_word_map[cur_id] = a
                cur_id += 1
            if b not in word_id_map:
                word_id_map[b] = cur_id
                id_word_map[cur_id] = b
                cur_id += 1
            a_id, b_id = word_id_map[a], word_id_map[b]
            uf.union(a_id, b_id)
        
        res = []
        words = text.split(' ')
        n = len(words)

        def dfs(index, words):
            if index == n: 
                res.append(' '.join(words ))
                return 
            else:
                for i in range(index, len(words)):
                    temp = words[i]
                    if temp not in word_id_map:
                        continue
                    word_parent = uf.find(word_id_map[temp])
                    for j, _ in enumerate(uf.root):
                        root_j = uf.find(j)
                        if root_j == word_parent and temp != id_word_map[j]:
                            words[i] = id_word_map[j]
                            dfs(i + 1, words)
                    words[i] = temp 
                res.append(' '.join(words))

        dfs(0, words)
        return sorted(res)