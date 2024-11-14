class Solution:
    def largestAltitude(self, gains: List[int]) -> int:
        prev = 0
        highest_gain = 0
        for gain in gains:
            prev = prev + gain
            highest_gain = max(prev, highest_gain)
        return highest_gain
