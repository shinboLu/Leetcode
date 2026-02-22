class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        _zip = []
        for time, user, web in zip(timestamp, username, website):
            _zip.append([time, user, web])
        _zip.sort(key = lambda x: x[0])

        user_website_map = collections.defaultdict(list)

        for _, user, web in _zip:
            user_website_map[user].append(web)

        scores = collections.defaultdict(int)

        for user in user_website_map:
            routes = set(combinations(user_website_map[user],3))
            for route in routes:
                scores[route] += 1
        max_val = max(scores.values())
        res = []
        for route, score in scores.items():
            if score == max_val:
                res.append(route)
        if len(route) > 1:
            res.sort()

        return res[0]

        