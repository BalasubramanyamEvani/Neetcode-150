class MinStack:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.stack2 or val <= self.stack2[-1]:
            self.stack2.append(val)

    def pop(self) -> None:
        val = self.stack1.pop()
        if val == self.stack2[-1]:
            self.stack2.pop()
        return val

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()