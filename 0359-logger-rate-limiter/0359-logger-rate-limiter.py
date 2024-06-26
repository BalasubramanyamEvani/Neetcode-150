class Logger:
    def __init__(self, t=10):
        self.t = t
        # self.messages = {}
        self.messages = deque()
        self.uniq_elements = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Hashmap Solution
        
        # if message not in self.messages or self.messages[message] <= timestamp:
        #     self.messages[message] = timestamp + self.limiter
        #     return True
        # return False
        
        # Queue solution - better since old messages can also be deleted while checking
        # while loop to discard old elements
        while self.messages and self.messages[0][1] <= timestamp:
            msgItem = self.messages.popleft()
            self.uniq_elements.remove(msgItem[0])
        # now new message not in queue can print it
        if message not in self.uniq_elements:
            # works because chronological order
            self.messages.append((message, timestamp + self.t))
            self.uniq_elements.add(message)
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)