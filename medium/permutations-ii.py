class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # sort and then only count the first of each number

        nums.sort()
        res = []
        path = []
        explored = set()
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
            else:
                prev = None
                for i in range(len(nums)):
                    if i in explored:
                        continue
                    if nums[i] != prev:
                        prev = nums[i]
                        explored.add(i)
                        path.append(nums[i])
                        dfs()
                        path.pop()
                        explored.remove(i)
        
        dfs()
        return res