# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

from collections import defaultdict

class TimeMap(object):

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.values[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        l, r = 0, len(self.values[key]) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if self.values[key][m][0] == timestamp:
                return self.values[key][m][1]
            elif self.values[key][m][0] > timestamp:
                r = m - 1
            else:
                res = self.values[key][m][1]
                l = m + 1
        
        return res