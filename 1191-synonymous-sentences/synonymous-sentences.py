class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        G = defaultdict(set)
        for x,y in synonyms:
            G[x].add(y)
            G[y].add(x)
        
        def dfs(w,ans):
            ans.add(w)
            for x in G[w]:
                if x not in ans: dfs(x,ans)
                    
        X = text.split()
        out = []
        for w in X:
            out1 = []
            if w in G:
                wset = set()
                dfs(w, wset)
                for w1 in wset:
                    if out: out1.extend([x+" "+w1 for x in out])
                    else: out1.append(w1)
            else: out1 = [x+" "+w for x in out] if out else [w]
            out = out1
        return sorted(out)
        