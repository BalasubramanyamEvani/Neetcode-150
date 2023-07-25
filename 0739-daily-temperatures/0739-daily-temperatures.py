class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_stack = collections.deque()
        def add_to_stack(idx):
            while max_stack and temperatures[max_stack[-1]] <=  temperatures[idx]:
                max_stack.pop()
            next_warmer_id = 0
            if max_stack:
                next_warmer_id = max_stack[-1] - idx
            max_stack.append(idx)
            return next_warmer_id
        
        ret = []
        for i in range(len(temperatures) - 1, -1, -1):
            next_warmer_id = add_to_stack(i)
            ret.append(next_warmer_id)
        return ret[::-1]
        