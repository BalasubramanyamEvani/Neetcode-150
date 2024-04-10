class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        res = [0] * N
        # the sorted order
        deck = sorted(deck)
        # simulation using indices
        q = deque([i for i in range(N)])
        ptr = 0
        while q:
            # insert at respective positions
            # [0, 1, 2, 3, 4, 5, 6]
            # ✔︎ x ✔︎ x ✔︎ x ✔︎
            #   ✔︎   x   ✔︎
            #.      ✔︎   x
            #           ✔︎
            index = q.popleft()
            res[index] = deck[ptr]
            if q:
                q.append(q.popleft())
            ptr += 1
        return res
