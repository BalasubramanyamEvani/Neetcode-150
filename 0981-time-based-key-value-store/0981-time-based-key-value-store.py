class TimeMap:
    def __init__(self):
        self.versions = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.versions:
            self.versions[key] = [(timestamp, value)]
        else:
            self.versions[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
            if key not in self.versions:
                return ""
            if timestamp < self.versions[key][0][0]:
                return ""
            low = 0
            high = len(self.versions[key]) - 1
            index = -1
            while low <= high:
                mid = low + (high - low) // 2
                if self.versions[key][mid][0] == timestamp:
                    return self.versions[key][mid][1]
                if self.versions[key][mid][0] > timestamp:
                    high = mid - 1
                else:
                    index = mid
                    low = mid + 1
            return self.versions[key][index][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)