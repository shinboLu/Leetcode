class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        combs = []
        for user, time, web in zip(username, timestamp, website):
            combs.append([time, user, web])
        combs.sort(key = lambda x:x[0])

        user_web = collections.defaultdict(list)
        for _, user, web in combs:
            user_web[user].append(web)
        print(user_web)
        scores = collections.defaultdict(int)

        for user in user_web:
            choices = set(combinations(user_web[user], 3))
            for choice in choices:
                scores[choice] +=1
        
        max_val = max(scores.values())
        res = []
        for route, score in scores.items():
            if score == max_val:
                res.append(route)
        
        res.sort()
        return res[0]
            
            