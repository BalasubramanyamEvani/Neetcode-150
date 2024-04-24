class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        cur = [-math.inf, math.inf]

        for num in preorder:
            while stack and stack[-1][0] < num:
                temp = stack.pop()
                cur[0] = temp[0]
                cur[1] = temp[2]

            if not cur[0] < num < cur[1]:
                return False

            stack.append((num, *cur))
            cur[1] = num

        return True
