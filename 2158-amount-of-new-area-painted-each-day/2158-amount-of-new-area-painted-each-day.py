class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        dp = {}
        areas = []
        for start, end in paint:
            area = 0
            index = start
            while index < end:
                eindex = dp.get(index, -1)
                if eindex == -1:
                    area += 1
                    dp[index] = end - 1
                    index += 1
                else:
                    dp[index] = max(eindex, end - 1)
                    index = eindex + 1
            areas.append(area)
        return areas
