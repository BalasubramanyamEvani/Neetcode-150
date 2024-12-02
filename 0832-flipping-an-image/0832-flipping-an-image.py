class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        nr, nc = len(image), len(image[0])
        for row in range(nr):
            l, r = 0, nc - 1
            while l < r:
                image[row][r] = 1 - image[row][r]
                image[row][l] = 1 - image[row][l]
                image[row][r], image[row][l] = image[row][l], image[row][r]
                l += 1
                r -= 1
            if nc & 1:
                image[row][l] = 1 - image[row][l]
        return image
