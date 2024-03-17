class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        def merge():
            stack = deque()
            for interval in intervals:
                start, end = interval
                if stack and start >= stack[-1][0] and start <= stack[-1][1]:
                    startp, endp = stack.pop()
                    new_start, new_end = min(startp, start), max(end, endp)
                    stack.append((new_start, new_end))
                else:
                    stack.append(interval)
            return list(stack)
                    
        return merge()
