class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, num = coordinates[0], coordinates[1]
        num = int(num)
        if (ord(letter) - ord('a')) % 2 == 0:
            return num % 2 == 0
        return num % 2 != 0
