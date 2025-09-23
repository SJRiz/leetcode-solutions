"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

class Node:
    def __init__(self):
        self.pairs = {} # key (alphabet) -> value (node)

class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        curr = self.node

        for c in word:
            if c not in curr.pairs:
                new = Node()
                curr.pairs[c] = new
            curr = curr.pairs[c]
        
        curr.pairs[";"] = None # mark as a word
        

    def search(self, word: str) -> bool:
        curr = self.node

        for c in word:
            if c not in curr.pairs:
                return False
            curr = curr.pairs[c]
            
        return True if ";" in curr.pairs else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.node

        for c in prefix:
            if c not in curr.pairs:
                return False
            curr = curr.pairs[c]
            
        return True
        
    # Solution is O(n) time and O(t) space where n is the length of the word and t is the number of nodes