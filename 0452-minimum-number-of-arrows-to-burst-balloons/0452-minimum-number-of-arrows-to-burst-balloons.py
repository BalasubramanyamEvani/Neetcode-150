class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[0], x[1]))
        stack = deque()
        def ifoverlaps(p1, p2):
            return p2[0] >= p1[0] and p2[0] <= p1[1]
        
        for point in points:
            if stack and ifoverlaps(stack[-1], point):
                prev = stack.pop()
                new_start, new_end = max(prev[0], point[0]), min(prev[1], point[1])
                stack.append((new_start, new_end))
            else:
                stack.append(point)
        
        return len(stack)
