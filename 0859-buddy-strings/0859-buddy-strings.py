class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diffs = 0
        N = len(s)
        for i in range(N):
            if s[i] != goal[i]:
                diffs += 1
        # if everything matches perfectly
        # then if all unique then we can't swap
        # else if repeating we can swap
        if diffs == 0:
            return len(s) != len(set(s))
        # anagram case
        # if both are anagrams and diff is 2
        m1 = Counter(s)
        m2 = Counter(goal)
        if diffs == 2:
            return m1 == m2
        return False
        