class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mem = {
            5: 0,
            10: 0,
            20: 0
        }
        for bill in bills:
            mem[bill] += 1
            diff = bill - 5
            if diff == 5:
                if mem[diff] == 0:
                    return False
                mem[diff] -= 1
            elif diff == 15:
                if mem[10] > 0 and mem[5] > 0:
                    mem[10] -= 1
                    mem[5] -= 1
                elif mem[5] >= 3:
                    mem[5] -= 3
                else:
                    return False
        return True                
        