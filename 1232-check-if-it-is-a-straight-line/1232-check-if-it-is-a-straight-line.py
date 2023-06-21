class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def calslope(p1, p2):
            if p2[0] - p1[0] == 0:
                return inf
            return (p2[1] - p1[1])/(p2[0] - p1[0])
        initslope = calslope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            if calslope(coordinates[i], coordinates[i - 1]) != initslope:
                return False
        return True
    