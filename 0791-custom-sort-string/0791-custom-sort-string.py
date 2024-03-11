class Solution:
    def customSortString(self, order: str, s: str) -> str:
        heap = []
        mem = {}
        i = 0
        for ch in order:
            mem[ch] = i
            i += 1
        for ch in s:
            val = mem.get(ch, math.inf)
            heapq.heappush(heap, (val, ch))
        arr = []
        while heap:
            arr.append(heapq.heappop(heap)[1])
        return "".join(arr)
