# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:
    # Every open bracket is closed by the same type of close bracket.
    # Open brackets are closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.

# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:

        # We will put all open brackets in a stack. If the parenthesis are valid, then the corresponding closing bracket should be at the top of the stack
        stack = []
        bracket_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        for c in s:
            # If c is not an open bracket, put it in the stack
            if c not in bracket_map:
                stack.append(c)
            else:
                # If the corresponding bracket is at the top of the stack, then its valid so far. Remove it from the stack to analyze the next bracket
                if stack and bracket_map[c] == stack[-1]:
                    stack.pop()
                else:
                    # Any inconsistencies mean it's not valid
                    return False

        # If the stack is not empty, then its invalid
        return True if not stack else False
    
    # Solution is O(n) time.