class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        rooms = []
        for interval in intervals:
            if not rooms:
                heapq.heappush(rooms, interval[1])
            else:
                end_time = heapq.heappop(rooms)
                if interval[0] < end_time:
                    heapq.heappush(rooms, end_time)
                heapq.heappush(rooms, interval[1])
        return len(rooms)
