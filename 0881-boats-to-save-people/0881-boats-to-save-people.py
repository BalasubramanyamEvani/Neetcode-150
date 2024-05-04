class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            boats += 1
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
        return boats
        