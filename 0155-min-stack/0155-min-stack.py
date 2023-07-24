class MinStack:

    def __init__(self):
        self.norm_stack = collections.deque()
        self.min_stack = collections.deque()
        self.ptr = 0
        
    def push(self, val: int) -> None:
        self.norm_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.ptr += 1
            
    def pop(self) -> None:
        if self.ptr > 0:
            val = self.norm_stack.pop()
            if self.min_stack[-1] == val:
                self.min_stack.pop()
            self.ptr -= 1
        
    def top(self) -> int:
        return self.norm_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()