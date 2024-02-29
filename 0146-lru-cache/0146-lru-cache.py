class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return f"Node(key={self.key}, value={self.val})"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_head(self, key, val):
        newnode = Node(key, val)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        return newnode
    
    def move_to_head(self, node):
        if self.head == node or not node:
            return self.head
        prevnode = node.prev
        nextnode = node.next
        if prevnode:
            prevnode.next = nextnode
        else:
            self.head = nextnode
        node.prev = None
        if nextnode:
            nextnode.prev = prevnode
        else:
            self.tail = prevnode
        node.next = None
        return self.insert_at_head(node.key, node.val)

    def pop_from_tail(self):
        if not self.head:
            return -1
        tailnode = self.tail
        prevnode = self.tail.prev
        if prevnode:
            prevnode.next = None
        self.tail.prev = None
        self.tail = prevnode
        if not self.tail:
            self.head = None
        return tailnode.key
    
    def __str__(self):
        curr = self.head
        ret = []
        while curr:
            ret.append(curr.__repr__())
            curr = curr.next
        return " ".join(ret)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = Queue()
        self.mem = {}

    def get(self, key: int) -> int:
        if key in self.mem:
            node = self.mem[key]
            newnode = self.q.move_to_head(node)
            self.mem[key] = newnode
            return newnode.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            node = self.mem[key]
            node.val = value
            newnode = self.q.move_to_head(node)
            self.mem[key] = newnode
        else:
            if self.capacity == 0:
                oldkey = self.q.pop_from_tail()
                del self.mem[oldkey]
                self.capacity += 1
            self.mem[key] = self.q.insert_at_head(key, value)
            self.capacity -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)