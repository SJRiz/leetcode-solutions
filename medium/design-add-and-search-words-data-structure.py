"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""

class Node:
    def __init__(self):
        self.pairs = {}     # key (letter) -> value (node with corresponding letter)
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.node = Node()  # dummy node
        

    def addWord(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.pairs:
                curr.pairs[c] = Node()
            curr = curr.pairs[c]
        
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        # constraints say at most 2 dots. we'd have to check all posibilities with one dot (dfs)
        def dfs(curr, i):
            if i == len(word):
                return curr.is_end
            if word[i] == ".":
                for node in curr.pairs.values():
                    res = dfs(node, i+1)
                    if res == True:
                        return True
                return False
            elif word[i] not in curr.pairs:
                return False
            return dfs(curr.pairs[word[i]], i+1)
        
        return dfs(self.node, 0)
        
