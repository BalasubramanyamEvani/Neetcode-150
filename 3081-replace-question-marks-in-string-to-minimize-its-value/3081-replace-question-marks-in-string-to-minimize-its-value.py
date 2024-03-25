class Solution:
    def minimizeStringValue(self, s: str) -> str:
        heap = []
        mem = {}
        for i in range(97, 123):
            mem[chr(i)] = 0
        question_marks = []
        for i, ch in enumerate(s):
            if ch != "?":
                mem[ch] += 1
            else:
                question_marks.append(i)
        
        for k, v in mem.items():
            heapq.heappush(heap, (v, k))
        
        ret = [ch for ch in s]
        i, qN = 0, len(question_marks)
        extra_letters = []
        
        while i < qN:
            v, k = heapq.heappop(heap)
            extra_letters.append(k)
            heapq.heappush(heap, (v + 1, k))
            i += 1
        
        i = 0
        heapq.heapify(extra_letters)
        while extra_letters:
            ret[question_marks[i]] = heapq.heappop(extra_letters)
            i += 1
        
        return "".join(ret)
