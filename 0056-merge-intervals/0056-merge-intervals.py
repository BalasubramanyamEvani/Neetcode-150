class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        stack = deque()
        stack.append(intervals[0])
        N = len(intervals)
        for i in range(1, N):
            curr = intervals[i]
            prev = stack[-1]
            prev_start, prev_end, curr_start, curr_end = prev[0], prev[1], curr[0], curr[1]
            if curr_start <= prev_end:
                merged = [prev_start, max(curr_end, prev_end)]
                stack.pop()
                stack.append(merged)
            else:
                stack.append(curr)
        return list(stack)
