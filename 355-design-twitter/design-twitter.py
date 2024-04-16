class Tweet:
    def __init__(self, tweetId, time):
        self.tweetId = tweetId
        self.time = time
        self.next = None
    
    def __lt__(self, other):
        return (self.time > other.time)

class User:
    def __init__(self, userId):
        self.userId = userId
        self.followed = set()
        self.followed.add(userId)
        self.tweets = None
    
    def follow(self, followeeId):
        self.followed.add(followeeId)
    
    def unfollow(self, followeeId):
        if followeeId != self.userId and followeeId in self.followed:
            self.followed.remove(followeeId)
    
    def post(self, tweetId, time):
        new = Tweet(tweetId, time)
        new.next = self.tweets
        self.tweets = new

class Twitter:
    import heapq
    def __init__(self):
        self.timestamp = 0
        self.userMap = dict() # uderId --> User object

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 若 userId 不存在，则新建
        if userId not in self.userMap:
            self.userMap[userId] = User(userId)
        curUser = self.userMap[userId]
        curUser.post(tweetId, self.timestamp)
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.userMap:
            return []
        user = self.userMap[userId]
        result = []
        pq = []
        followeeIds = list(user.followed)
        for i in followeeIds:
            t = self.userMap[i].tweets
            if t:
                heapq.heappush(pq, t)
        while pq:
            if len(result) == 10:
                break
            t = heapq.heappop(pq)
            result.append(t.tweetId)
            if t.next:
                heapq.heappush(pq, t.next)
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # 若 follower 不存在，则新建
        if followerId not in self.userMap:
            self.userMap[followerId] = User(followerId)
        # 若 followee 不存在，则新建
        if followeeId not in self.userMap:
            self.userMap[followeeId] = User(followeeId)
        follower = self.userMap[followerId]
        follower.follow(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userMap:
            follower = self.userMap[followerId]
            follower.unfollow(followeeId)