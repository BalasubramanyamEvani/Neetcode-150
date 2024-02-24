class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        heights.append(-1)
        ret = -1
        for i, height in enumerate(heights):
            l = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                area = h * (i - j)
                ret = max(ret, area)
                l = j
            stack.append((height, l))
        return ret
