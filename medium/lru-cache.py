# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in O(1) average time complexity.

# We will use a doubly linked list for this problem, and a hashmap to store the keys which will point to each node.
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.pair = {}  # Each key will point to their respective node

        # Use dummy left and right nodes, these will be used to check the leftmost (lru) and rightmost (mru) values
        self.left, self.right = Node(None, None), Node(None, None)
        self.left.next = self.right
        self.right.prev = self.left
    
    # Helper function. Creates a node behind the right dummy node
    def insert_right(self, key, val):
        prv = self.right.prev
        node = Node(key, val)
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node

        # Update the key in the pair hashmap
        self.pair[key] = self.right.prev

    # Helper function. Removes a node
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key):
        if key in self.pair:
            node, val = self.pair[key], self.pair[key].val

            # If we get a value, then it becomes mru. Remove it and add it to the right
            self.remove(node)
            self.insert_right(key, val)
            return self.pair[key].val
        else:
            return -1
        
    def put(self, key, value):
        if key in self.pair:
            self.remove(self.pair[key]) # Remove the node and add it to the right if it already exists
        self.insert_right(key, value)
        
        # If we reach max capacity, delete the lru node (which is one right to the left dummy node) and its key from the hashmap
        if len(self.pair) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.pair[lru.key]

    # All functions are O(1) time, and solution is O(n) space complexity
        