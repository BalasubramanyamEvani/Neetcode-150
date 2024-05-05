class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        # sieve
        primes = [True for i in range(n)]
        primes[0], primes[1] = False, False 
        j = 2
        count = 0
        while j <= int(sqrt(n)):
            if primes[j]:
                for i in range(j * j, n, j):
                    primes[i] = False
            j += 1
        return sum(primes)
        
#         def isPrime(n):
#             if n <= 1:
#                 return False
#             if n <= 3:
#                 return True
#             if n % 2 == 0 or n % 3 == 0:
#                 return False
#             for i in range(5, int(sqrt(n)) + 1, 6):
#                 if n % i == 0 or n % (i + 2) == 0:
#                     return False
#             return True

#         count = 0
#         for i in range(1, n):
#             if isPrime(i):
#                 count += 1
#         return count
