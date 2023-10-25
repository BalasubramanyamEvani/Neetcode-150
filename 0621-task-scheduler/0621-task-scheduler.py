class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mem = {}
        for task in tasks:
            if task in mem:
                mem[task] += 1
            else:
                mem[task] = 1
        freq = [[-v, k] for k, v in mem.items()]
        heapq.heapify(freq)
        buffer = deque([])
        t = 0
        while freq or buffer:
            t += 1
            if buffer and buffer[0][2] == t:
                v, k, _ = buffer.popleft()
                heapq.heappush(freq, [v, k])
            
            if freq:
                v, k = heapq.heappop(freq)
                # print(k)
                v += 1
                if v != 0:
                    buffer.append([v, k, t + n + 1])
            # else:
                # print("idle")
        
        return t
