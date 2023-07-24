class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, ch):
        self.stack.append(ch)
    
    def pop(self):
        if not self.isEmpty():
            ch = self.stack[-1]
            self.stack.pop()
            return ch
    
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        chmap = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for ch in s:
            if stack.isEmpty():
                stack.push(ch)
            elif ch == "(" or ch == "{" or ch == "[":
                stack.push(ch)
            elif chmap[ch] == stack.top():
                stack.pop()
            else:
                return False
        return stack.isEmpty()