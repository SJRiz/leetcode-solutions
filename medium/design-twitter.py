"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
"""

from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.user_list = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.user_list[userId].add(userId)

        for following in self.user_list[userId]:
            for tweet in self.tweets[following]:
                heapq.heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
                    
        res = []

        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_list[followerId]:
            self.user_list[followerId].remove(followeeId)
