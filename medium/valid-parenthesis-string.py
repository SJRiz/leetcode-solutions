class Solution:
    def checkValidString(self, s: str) -> bool:
        # we track 2 stacks, one for the brackets and one for the stars
        # each stack will also track the index too
        # if we encounter a closing bracket, it will remove stars that are before the index
        # at the end we do a cleanup; this time stars will only remove opening brackets if the index is after

        brackets = []
        stars = []

        for i in range(len(s)):
            # i is index, c is actual char
            c = s[i]

            if c == "(":
                brackets.append((c, i))
            elif c == ")":
                if not brackets:
                    if not stars:
                        return False
                    stars.pop()
                else:
                    brackets.pop()
            else:
                stars.append((c,i))
        
        # cleanup
        while stars:
            if not brackets:
                return True
            _, i = stars.pop()
            if i > brackets[-1][1]:
                brackets.pop()
        
        return False if brackets else True

