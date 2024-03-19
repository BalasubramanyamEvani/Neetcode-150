class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mem = {}
        for task in tasks:
            mem[task] = mem.get(task, 0) + 1
        task_heap = [[-v, k] for k, v in mem.items()]
        heapq.heapify(task_heap)
        buffer = deque()
        t = 0
        while task_heap or buffer:
            t += 1
            if buffer and buffer[0][2] == t:
                v, k, _ = buffer.popleft()
                heapq.heappush(task_heap, [v, k])
            
            if task_heap:
                v, k = heapq.heappop(task_heap)
                v += 1
                if v != 0:
                    buffer.append([v, k, t + n + 1])
            # else:
                # print("idle")
        
        return t
