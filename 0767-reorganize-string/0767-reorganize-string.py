class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(heap)
        ret = []
        while heap:
            c1, char1 = heapq.heappop(heap)
            if not ret or ret[-1] != char1:
                ret.append(char1)
                c1 += 1
            elif not heap:
                ret = []
                break
            else:
                c2, char2 = heapq.heappop(heap)
                ret.append(char2)
                c2 += 1
                if c2 != 0:
                    heapq.heappush(heap, (c2, char2))
            if c1 != 0:
                heapq.heappush(heap, (c1, char1))
        return "".join(ret)
