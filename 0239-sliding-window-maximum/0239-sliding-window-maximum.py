class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        monotonic_decreasing_q = collections.deque()
        def add_to_q(idx):
            while len(monotonic_decreasing_q) > 0 and nums[monotonic_decreasing_q[-1]] < nums[idx]:
                monotonic_decreasing_q.pop()
            monotonic_decreasing_q.append(idx)
        
        l = 0
        r = 0
        ret = []
        while r < nums_len:
            add_to_q(r)
            win_len = r - l + 1
            
            if monotonic_decreasing_q[0] < l:
                monotonic_decreasing_q.popleft()
            
            if win_len == k:
                curr_max = monotonic_decreasing_q[0] 
                ret.append(nums[curr_max])
                l += 1
            r += 1
        return ret
