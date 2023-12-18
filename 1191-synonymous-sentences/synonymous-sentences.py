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

        def backtrack(index, combs):
            res.append(' '.join(combs))
            
            for i in range(index, n):
                cur_word = words[i]
                if cur_word not in word_id_map:
                    continue

                cur_root = uf.find(word_id_map[cur_word])
                for j, _ in enumerate(uf.root):
                    root_j = uf.find(j)
                    if root_j == cur_root and cur_word != id_word_map[j]:
                        words[i] = id_word_map[j]
                        backtrack(i+1, words )
                words[i] = cur_word

                
        backtrack(0, words)

        return sorted(res)
