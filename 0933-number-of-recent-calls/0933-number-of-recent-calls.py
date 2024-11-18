class RecentCounter:

    def __init__(self):
        self._pings = deque()

    def ping(self, t: int) -> int:
        low = t - 3000
        while self._pings and self._pings[0] < low:
            self._pings.popleft()
        
        self._pings.append(t)
        return len(self._pings)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)