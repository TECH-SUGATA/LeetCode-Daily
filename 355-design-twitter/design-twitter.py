
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following[userId] | {userId}

        heap = []

        for user in users:
            for time, tweetId in self.tweets[user][-10:]:
                heapq.heappush(heap, (-time, tweetId))

        result = []

        for _ in range(10):
            if not heap:
                break

            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
