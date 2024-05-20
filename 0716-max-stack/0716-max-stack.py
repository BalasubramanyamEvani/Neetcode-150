class MaxStack:
    def __init__(self):
        self.heap = []
        self.stack = []
        self.uid = 0
        self.removed = set()
    
    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.uid))
        self.stack.append((x, self.uid))
        self.uid += 1
        
    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, uid = self.stack.pop()
        self.removed.add(uid)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]
    
    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        num, uid = heapq.heappop(self.heap)
        self.removed.add(-uid)
        return -num

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()