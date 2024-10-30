class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # greedy
        if n == 0:
            return True
        for i, num in enumerate(flowerbed):
            if num == 0:
                if i > 0 and flowerbed[i - 1] == 1 or i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                    continue
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
        return False
