class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        visited = set()
        while q:
            word = q.popleft()
            if not word:
                return True
            if word not in visited:
                visited.add(word)
                for val in wordDict:
                    if word.startswith(val):
                        q.append(word[len(val):])
        return False
