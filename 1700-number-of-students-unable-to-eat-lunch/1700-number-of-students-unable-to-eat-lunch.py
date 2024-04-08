class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        count = len(q)
        itr = 0
        top = 0
        while q and itr != count:
            preference = q.popleft()
            if preference == sandwiches[top]:
                top += 1
                count -= 1
                itr = 0
            else:
                q.append(preference)
                itr += 1
        return len(q)
