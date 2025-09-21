from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}

        for t in tokens:
            if t in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                if t == '+':
                    stack.append(num1 + num2)
                elif t == '-':
                    stack.append(num1 - num2)
                elif t == '*':
                    stack.append(num1 * num2)
                elif t == '/':
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(t))
        
        return stack[-1]
    
    # Solution is O(n) time and O(n) space