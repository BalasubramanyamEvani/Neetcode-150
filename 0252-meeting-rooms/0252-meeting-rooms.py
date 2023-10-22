class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        heapq.heapify(intervals)
        prev = heapq.heappop(intervals) 
        while intervals:
            curr = heapq.heappop(intervals)
            if curr[0] < prev[1]:
                return False
            prev = curr
        return True
