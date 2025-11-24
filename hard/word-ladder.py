from typing import List
from collections import defaultdict, deque

"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # you can make an undirected graph with the words
        # e.x. from cat, you connect it to every word where only 1 character is mismatched
        # (in this case it would be bat)
        # do the same process to bat (should connect to bag and cat)
        # i think this is a bfs problem

        if endWord not in wordList:
            return 0
        seen = set()

        sequences = defaultdict(set)

        l = len(beginWord)

        for w in wordList:
            for i in range(l):
                key = (w[0:i] + " " + ("" if i+1 == l else w[i+1:]))
                sequences[key].add(w)

        deq = deque([beginWord])
        level = 1

        while deq:
            for _ in range(len(deq)):
                wrd = deq.popleft()

                if wrd in seen:
                    continue

                seen.add(wrd)

                for i in range(l):
                    key = (wrd[0:i] + " " + ("" if i+1 == l else wrd[i+1:]))
                    if endWord in sequences[key]:
                        return level+1
                    for w in sequences[key]:
                        if w not in seen:
                            deq.append(w)

                
            level += 1
        
        return 0
                        
                