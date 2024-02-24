class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        def addq(num, i):
            while q and q[-1][0] < num:
                q.pop()
            q.append((num, i))
        l = 0
        r = 0
        N = len(nums)
        ret = []
        while r < N:
            window = r - l + 1
            addq(nums[r], r)
            if window == k:
                ret.append(q[0][0])
                if q[0][1] == l:
                    q.popleft()
                l += 1
            r += 1
        return ret
