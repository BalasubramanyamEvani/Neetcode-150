class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = -math.inf
        l, r = 0, len(height) - 1
        while l < r:
            currarea = abs(l - r) * min(height[l], height[r])
            maxarea = max(maxarea, currarea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea
