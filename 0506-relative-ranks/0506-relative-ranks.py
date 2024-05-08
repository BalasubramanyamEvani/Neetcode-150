class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        N = len(scores)
        heap = [(-num, i) for i, num in enumerate(scores)]
        heapq.heapify(heap)
        ret = [""] * N
        mem = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal"
        }
        ptr = 1
        while heap:
            _, position = heapq.heappop(heap)
            if ptr in mem:
                ret[position] = mem[ptr]
            else:
                ret[position] = str(ptr)
            ptr += 1
        return ret
