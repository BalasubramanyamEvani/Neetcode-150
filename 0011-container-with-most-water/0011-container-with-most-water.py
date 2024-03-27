class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = -1
        l = 0
        r = len(height) - 1
        while l < r:
            currarea = (r - l) * min(height[l], height[r])
            maxarea = max(maxarea, currarea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea
    