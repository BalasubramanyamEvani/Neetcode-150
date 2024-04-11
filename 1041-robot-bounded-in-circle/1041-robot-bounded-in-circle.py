class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        rot = 0
        # because after 4 iterations it should be
        # facing the same way and so we can compare it
        for i in range(4):
            for instruction in instructions:
                if instruction == "R":
                    rot = (rot + 1) % 4
                elif instruction == "L":
                    rot = (rot - 1) % 4
                else:
                    x += directions[rot][0]
                    y += directions[rot][1]
        
        return x == 0 and y == 0
