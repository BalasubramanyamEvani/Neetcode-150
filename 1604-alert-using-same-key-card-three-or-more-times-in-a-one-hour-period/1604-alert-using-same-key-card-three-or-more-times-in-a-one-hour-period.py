import heapq as hq

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        for i, t in enumerate(keyTime):
            h, m = t.split(":")
            keyTime[i] = int(h) * 60 + int(m)
        
        def check_within_hr(t1, t2, t3):
            return t2 - t1 <= 60 and t3 - t2 <= 60 and t3 - t1 <= 60
        
        mem = {}
        res = set()
        sorted_keys = sorted(zip(keyName, keyTime), key=lambda x: x[1])
        for k in sorted_keys:
            name, time = k[0], k[1]
            if name not in mem:
                mem[name] = []
            heapq.heappush(mem[name], time)
            if len(mem[name]) == 3:
                t1 = heapq.heappop(mem[name])
                t2 = heapq.heappop(mem[name])
                t3 = heapq.heappop(mem[name])
                if check_within_hr(t1, t2, t3):
                    res.add(name)
                heapq.heappush(mem[name], t2)
                heapq.heappush(mem[name], t3)

        return list(sorted(res))
                