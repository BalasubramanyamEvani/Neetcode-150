class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited_rooms = {i: False for i in range(N)}
        q = deque([0])
        while q:
            room = q.popleft()
            visited_rooms[room] = True
            for dst in rooms[room]:
                if not visited_rooms[dst]:
                    q.append(dst)
        for visited_status in visited_rooms.values():
            if not visited_status:
                return False
        return True
