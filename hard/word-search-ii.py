from typing import List

"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # turn the words into a trie
        # we can brute force to find words, but backtrack if it doesnt exist in the trie

        # b -> a
        # a -> t, c

        # trie is just a hashmap pointing to another hashamp
        class Node:
            def __init__(self, val=""):
                self.value = val
                self.nxt = {}

        class Trie:
            def __init__(self):
                node = Node()
                self.node = node
            
            def add(self, word):
                curr = self.node
                for c in word:
                    if c not in curr.nxt:
                        new = Node(c)
                        curr.nxt[c] = [new, 0]
                    curr.nxt[c][1] += 1
                    curr = curr.nxt[c][0]
            
            def delete(self, word):
                curr = self.node
                for c in word:
                    curr.nxt[c][1] -= 1
                    curr = curr.nxt[c][0]
            
            def search(self, word):
                # -1 -> not found, 0 -> partial find, 1 -> word found
                curr = self.node
                for c in word:
                    if c not in curr.nxt or curr.nxt[c][1] <= 0:
                        return -1
                    curr = curr.nxt[c][0]
                if "." in curr.nxt and curr.nxt["."][1] > 0:
                    return 1
                else:
                    return 0
            
        trie = Trie()
        for word in words:
            trie.add(word+".")
        
        res = []
        def backtrack(x, y, chrs):
            if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or (x,y) in seen:
                return

            new = chrs + board[x][y]

            found = trie.search(new)
            if found == 1:
                res.append(new)
                trie.delete(new+".")
            elif found == -1:
                return
            
            seen.add((x,y))
            backtrack(x+1, y, new)
            backtrack(x-1, y, new)
            backtrack(x, y+1, new)
            backtrack(x, y-1, new)
            seen.remove((x,y))
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                seen = set()
                backtrack(x, y, "")

        return res

                

        


                        