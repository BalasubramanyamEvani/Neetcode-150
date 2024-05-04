class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        def lt(a, b):
            return abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b) 
        
        def bsearch(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] > x:
                    r = mid - 1
                elif arr[mid] < x:
                    if mid + 1 < N and lt(arr[mid], arr[mid + 1]):
                        break
                    else:
                        l = mid + 1
                else:
                    if mid - 1 >= 0 and arr[mid - 1] == x:
                        r = mid - 1
                    else:
                        break
            return mid
        
        index = bsearch(0, N - 1)
        l, r = index, index + 1
        while k > 0:
            if l == -1:
                r += 1
                k -= 1
                continue
            if r == N or lt(arr[l], arr[r]):
                l -= 1
            else:
                r += 1
            k -= 1
        return arr[l + 1: r]
