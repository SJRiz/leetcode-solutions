class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        # build backwards and forwards
        # a subseq cannot start between t[0] and t[-1], as the score will always result in len(t)

        l = 0
        r = len(t) - 1
        leftmost = [0] * len(s)

        # first pass: build from the left
        for i in range(len(s)):
            c = s[i]
            if l < len(t) and t[l] == c:
                l += 1
            leftmost[i] = l
            if l == len(t):
                return 0

        # Initialize score assuming we just keep the best prefix and delete the rest
        score = len(t) - leftmost[-1]

        # second pass: build from the right
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            
            if r >= 0 and t[r] == c:
                r -= 1
            
            # Use the prefix matched BEFORE the current character to avoid double-counting s[i]
            left_match = leftmost[i - 1] if i > 0 else 0
            
            if left_match > r:
                return 0
                
            score = min(score, r - left_match + 1)

        return score