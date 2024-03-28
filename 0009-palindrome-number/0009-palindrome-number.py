class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        def reverse(num):
            ret = 0
            num_digits = int(math.log10(num)) + 1
            while num > 0:
                rem = num % 10
                ret += rem * (10**(num_digits - 1))
                num = num // 10
                num_digits -= 1
            return ret
        
        reversed_x = reverse(x)
        return reversed_x == x
