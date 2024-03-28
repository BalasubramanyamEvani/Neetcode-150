class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # possible remainders = {-1, 0, 1}
        def convert_to_base10(num):
            n = len(num)
            base = -2
            ret = 0
            for i in range(n):
                ret += num[i] * (base**(n - i - 1))
            return ret
        
        def convert_to_baseneg2(num):
            if num == 0:
                return [num]
            base = -2
            ret = []
            while num != 0:
                rem = num % base
                num = num // base
                if rem == -1:
                    rem = 1
                    num += 1
                ret.append(rem)
            return ret[::-1]
            
        n1 = convert_to_base10(arr1)
        n2 = convert_to_base10(arr2)
        
        base10_result = n1 + n2
        return convert_to_baseneg2(base10_result)
