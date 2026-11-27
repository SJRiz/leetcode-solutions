class Solution:
    def canAliceWin(self, n: int) -> bool:
        # can we solve this in O(1) time???
        # kinda, u can do O(10) which is O(1)
        remaining = n
        for i in range(10, 0, -1):
            remaining -= i
            if remaining < 0:
                return False if i % 2 == 0 else True
        
        return True