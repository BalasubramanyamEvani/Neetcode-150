class Solution:
    def isHappy(self, n: int) -> bool:
        def getnext(n):
            ret = 0
            while n > 0:
                rem = n % 10
                ret += rem**2
                n = n // 10
            return ret
        slow = n
        fast = getnext(n)
        while slow != fast and fast != 1:
            slow = getnext(slow)
            fast = getnext(getnext(fast))
        return fast == 1
