class Item:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mem = Counter(words)
        heap = []
        for word, freq in mem.items():
            heapq.heappush(heap, Item(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        heap = sorted(heap, key=lambda x: (-x.freq, x.word))
        return [item.word for item in heap]
