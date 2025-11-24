from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # since a queen can attack horiz, vert, and diag,
        # then each queen must be on their own horiz, vert, and diag
        # we backtrack if there is no other possible space to fill, or if we successfully places n queens

        vert = set()        # -> 0, n-1
        neg_diag = set()    # to calculate this, we know y = x + b for all diagonals. Thus, b = y - x.
        pos_diag = set()    # y = -x + b, b = y + x

        res = []
        path = []

        def backtrack(x, y, cnt):
            if x >= n:
                return

            row = "."*(y) + "Q" + "."*(n-y-1)
            path.append(row)

            if x == n-1 and cnt == n-1:
                res.append(path[:])
                path.pop()
                return

            vert.add(y)
            pos_diag.add(y-x)
            neg_diag.add(y+x)

            for i in range(n):
                if not (i in vert or i-(x+1) in pos_diag or i+(x+1) in neg_diag):
                    backtrack(x+1, i, cnt+1)

            path.pop()
            vert.remove(y)
            pos_diag.remove(y-x)
            neg_diag.remove(y+x)
        
        for i in range(n):
            backtrack(0, i, 0)
        
        return res
        


            