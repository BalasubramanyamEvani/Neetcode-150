class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors_of(num):
            divisors = 0
            counts = 0
            for d in range(1, int(math.sqrt(num)) + 1):
                if num % d == 0:
                    divisors += d
                    other = num // d
                    if other != d:
                        divisors += other
                        counts += 2
                    else:
                        counts += 1
            return divisors if counts == 4 else 0

        mem = {}
        ret = 0
        for num in nums:
            if num not in mem:
                mem[num] = divisors_of(num)
            ret += mem[num]
        return ret
