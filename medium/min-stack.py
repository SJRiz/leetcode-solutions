# Design a stack class that supports the push, pop, top, and getMin operations.

    # MinStack() initializes the stack object.
    # void push(int val) pushes the element val onto the stack.
    # void pop() removes the element on the top of the stack.
    # int top() gets the top element of the stack.
    # int getMin() retrieves the minimum element in the stack.

# Each function should run in O(1) time.

class MinStack:
    
    # We will store minimum numbers in a stack as well.
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:

        # If the pushed val is smaller than any value in the min_stack, then push it to the min_stack as well
        # This number will be the next "local minimum" for the numbers ahead until another minimum is pushed
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:

        # If the number being popped is also the minimum, remove that number (the next number in the stack is the new minimum)
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]