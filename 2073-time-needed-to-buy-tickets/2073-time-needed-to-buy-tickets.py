class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i, ticket in enumerate(tickets):
            # the number of times the front numbers
            # would come infront of the ticket at kth
            # position
            if i <= k :
                res += min(ticket, tickets[k])
            # the number of times the back numbers
            # would come behind the ticket at kth
            # position (-1)
            else:
                res += min(tickets[k] - 1, ticket)
        return res
