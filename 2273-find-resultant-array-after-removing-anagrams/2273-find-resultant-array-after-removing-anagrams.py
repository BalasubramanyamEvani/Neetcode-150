class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = deque()
        def are_anagrams(w1, w2):
            return Counter(w1) == Counter(w2)

        for word in words:
            if not stack or not are_anagrams(word, stack[-1]):
                stack.append(word)
        return list(stack)
