class LargerNum(str):
    def __lt__(a, b):
        return a + b > b + a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        A = nums
        B = [str(num) for num in A]
        B = sorted(B, key=LargerNum)
        res = "".join(B)
        return res if int(res) != 0 else "0"
