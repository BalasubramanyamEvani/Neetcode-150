class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def can_catch_up(ahead, behind):
            p1, p2 = ahead[0], behind[0]
            s1, s2 = ahead[1], behind[1]
            delta1 = target - p1
            delta2 = target - p2
            return delta2 / s2 <= delta1 / s1
            
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs = sorted(pairs, key=lambda x: x[0])
        stack = deque()
        N = len(pairs)
        for i in range(N - 1, -1, -1):
            behind = pairs[i]
            if not stack or not can_catch_up(stack[-1], behind):
                stack.append(behind)
        return len(stack)
