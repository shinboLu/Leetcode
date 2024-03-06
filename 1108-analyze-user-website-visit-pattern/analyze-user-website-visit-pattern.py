class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        d = collections.defaultdict(list)
        c = collections.Counter()            
        for u, t, w in zip(username, timestamp, website): 
            d[u].append((t, w))
            c[u] += 1
        three_seq_cnt = collections.defaultdict(int)  
        for u, records in d.items():            
            records.sort()                            
            visited = set()                           
            for i in range(c[u]):                     
                for j in range(i+1, c[u]):
                    for k in range(j+1, c[u]):
                        three_seq = (records[i][1], records[j][1], records[k][1])
                        if three_seq in visited: 
                            continue  
                        three_seq_cnt[three_seq] += 1
                        visited.add(three_seq)
                    
        ans = sorted(three_seq_cnt.items(), reverse=True, key=lambda x: (-x[1], x[0]))
        return ans[-1][0]