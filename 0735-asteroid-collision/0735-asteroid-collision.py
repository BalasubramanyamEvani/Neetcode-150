class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                if not stack:
                    # knocked out everything
                    stack.append(num)
                elif stack[-1] == abs(num):
                    # same magnitude
                    stack.pop()
                elif stack[-1] > abs(num):
                    # greater magnitude at the top
                    continue
                else:
                    # same negative sign
                    stack.append(num)
        return list(stack)
