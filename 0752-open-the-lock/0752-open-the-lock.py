class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = defaultdict(bool)
        q = deque()
        deadends = set(deadends)
        
        def rotate_wheel(string, index):
            num_string = [int(ch) for ch in string]
            num = num_string[index]
            prev, following = (num - 1) % 10, (num + 1) % 10
            
            num_string[index] = prev
            prev_num_string = "".join([str(n) for n in num_string])
            num_string[index] = following
            following_num_string = "".join([str(n) for n in num_string])
            
            return prev_num_string, following_num_string
            
        start = "0000"
        q.append((start, 0))
        visited[start] = True
        while q:
            curr, dist = q.popleft()
            if curr == target:
                return dist
            if curr in deadends:
                continue
            for i in range(4):
                n1, n2 = rotate_wheel(curr, i)
                if not visited[n1]:
                    visited[n1] = True
                    q.append((n1, dist + 1))
                if not visited[n2]:
                    visited[n2] = True
                    q.append((n2, dist + 1))
        return -1
