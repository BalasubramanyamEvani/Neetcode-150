class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        res = [0] * N
        deck = sorted(deck)
        q = deque([i for i in range(N)])
        ptr = 0
        while q:
            index = q.popleft()
            res[index] = deck[ptr]
            if q:
                q.append(q.popleft())
            ptr += 1
        return res
