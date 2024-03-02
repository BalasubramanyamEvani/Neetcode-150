class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Two pass solution
        
        # ones = 0
        # N = len(s)
        # for ch in s:
        #     if ch == "1":
        #         ones += 1
        # lsb = 1 if ones >= 1 else 0
        # zeros = N - ones
        # ones = ones - lsb
        # return "1" * ones + "0" * zeros + "1" * lsb
        
        # One pass solution
        N = len(s)
        l = 0
        r = N - 1
        arr = [ch for ch in s]
        while l <= r:
            if arr[l] == "1":
                l += 1
            if arr[r] == "0":
                r -= 1
            if l <= r and arr[l] < arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        last_one = l - 1
        if last_one >= 0 and last_one != N - 1:
            arr[last_one] = "0"
            arr[-1] = "1"
        return "".join(arr)
