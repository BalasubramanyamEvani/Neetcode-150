class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = -1
        rmax = -1
        num_heights = len(height)
        
        lmaxes = [-1] * num_heights
        rmaxes = [-1] * num_heights
        
        lmaxes[0] = -1
        for i in range(1, num_heights):
            lmax = max(lmax, height[i - 1])
            lmaxes[i] = lmax 
        
        rmaxes[-1] = rmax
        for i in range(num_heights - 2, -1, -1):
            rmax = max(rmax, height[i + 1])
            rmaxes[i] = rmax 
        
        counts = [0] * num_heights
        for i in range(num_heights):
            boundary = min(lmaxes[i], rmaxes[i])
            if boundary <= 0 or boundary <= height[i]:
                continue
            counts[i] = boundary - height[i]
        
        return sum(counts)
        