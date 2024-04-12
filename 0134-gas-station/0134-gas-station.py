class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot_gas, tot_cost = sum(gas), sum(cost)
        if tot_gas < tot_cost:
            return -1
        
        tot = 0
        N = len(gas)
        start = 0
        for i in range(N):
            # at each starting position
            # calculate the diff in the amount
            # of gas we get for travelling to next position
            # and the cost it takes to go to next position
            tot += gas[i] - cost[i]
            if tot < 0:
                # can't be the starting position
                tot = 0
                start = i + 1
        return start
