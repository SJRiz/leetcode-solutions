class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we will do O(1) extra space.
        # break into cyclic subgroups. 
        
        n = len(nums)
        cycle_length = n//math.gcd(n,k)
        num_cycles = n//cycle_length

        print(cycle_length, num_cycles)

        for i in range(num_cycles):
            curr, val = i, nums[i]
            for j in range(cycle_length):
                next = nums[(curr+k)%n]
                nums[(curr+k)%n] = val
                curr, val = (curr+k)%n, next
