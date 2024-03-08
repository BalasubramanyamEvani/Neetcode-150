class Logger:
    def __init__(self, limiter=10):
        self.limiter = limiter
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages or self.messages[message] <= timestamp:
            self.messages[message] = timestamp + self.limiter
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)