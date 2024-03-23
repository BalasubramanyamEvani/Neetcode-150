class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def overlaps(p1, p2):
            return p2[0] >= p1[0] and p2[0] < p1[1]
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        stack = deque()
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if not overlaps(stack[-1], interval):
                    stack.append(interval)
                elif overlaps(stack[-1], interval) and stack[-1][1] > interval[1]:
                    stack.pop()
                    stack.append(interval)
        return len(intervals) - len(stack)
