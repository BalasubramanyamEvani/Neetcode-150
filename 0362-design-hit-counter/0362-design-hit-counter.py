class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        low = 0
        high = len(self.hits) - 1
        target = timestamp - 300

        while low <= high:
            mid = low + (high - low) // 2
            if self.hits[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        
        return len(self.hits) - low


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)