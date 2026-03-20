class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        utw_list = []
        for time, user, web in zip(timestamp, username, website):
            utw_list.append([time, user, web])
        utw_list.sort(key = lambda x: x[0])
        
        uw_map = collections.defaultdict(list)

        for _, user, web in utw_list:
            uw_map[user].append(web)

        scores = collections.defaultdict(int)

        for user in uw_map:
            combs = set(combinations(uw_map[user], 3))
            for comb in combs:
                scores[comb] +=1

        max_val = max(scores.values())
        res = []

        for comb, count in scores.items():
            if count == max_val:
                res.append(comb) 

        res.sort()
        return res[0]
            
