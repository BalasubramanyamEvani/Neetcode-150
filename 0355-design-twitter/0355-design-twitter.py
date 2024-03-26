class Twitter:
    def __init__(self):
        self.tweets = {}
        self.social_graph = {}
        self.timestamp = 0
        self.topk = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.tweets:
            self.tweets[userId] = []

        self.timestamp += 1
        if len(self.tweets[userId]) < self.topk:
            heapq.heappush(self.tweets[userId], (self.timestamp, tweetId))
        elif self.timestamp > self.tweets[userId][0][0]:
            heapq.heappop(self.tweets[userId])
            heapq.heappush(self.tweets[userId], (self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        itr = 0
        minHeap = []
        # user tweets
        feeds = [self.tweets[userId]] if userId in self.tweets else []
        # user followee tweets
        if userId in self.social_graph:
            for followeeId in self.social_graph[userId]:
                if followeeId in self.tweets:
                    feeds.append(self.tweets[followeeId])
        # min heap to find topk recent by traversing all, at max every feed
        # would have self.topk posts
        for feed in feeds:
            for timestamp, tweetId in feed:
                if len(minHeap) < self.topk:
                    heapq.heappush(minHeap, (timestamp, tweetId))
                elif self.timestamp > minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (timestamp, tweetId))
        # need to return it from most recent to least recent
        # so pop from min heap and keep appending left
        result = deque()
        while minHeap:
            _, tweetId = heapq.heappop(minHeap)
            result.appendleft(tweetId)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.social_graph:
            self.social_graph[followerId] = set()

        self.social_graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.social_graph:
            return
        
        if not followeeId in self.social_graph[followerId]:
            return
        
        self.social_graph[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)