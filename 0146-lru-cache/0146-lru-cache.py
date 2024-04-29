class CacheItem:
    def __init__(
        self,
        key: int,
        val: int,
        prevPtr: "CacheItem" = None,
        nextPtr: "CacheItem" = None,
    ) -> None:
        self.key = key
        self.val = val
        self.nextPtr = nextPtr
        self.prevPtr = prevPtr

    def __str__(self) -> str:
        return f"[CacheItem(prev={self.prevPtr}, key={self.key}, val={self.val}, next={self.nextPtr.key}]"


class CacheQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.capacity = 0

    def appendleft(self, key: int, val: int) -> CacheItem:
        item = CacheItem(key, val)
        # increment size
        self.capacity += 1
        # if head is not present
        if not self.head:
            self.head = item
            self.tail = item
            return item
        # if head is present
        item.nextPtr = self.head
        self.head.prevPtr = item
        self.head = item
        return item

    def remove(self, item: CacheItem) -> tuple[int, int]:
        # trying to remove when queue is empty
        if self.capacity == 0:
            raise RuntimeError(f"Invalid operation remove for item: {item}")

        nextItem = item.nextPtr
        prevItem = item.prevPtr
        # if prev item is present connect to item.next
        if prevItem:
            prevItem.nextPtr = nextItem
        # else its head so update head
        else:
            self.head = nextItem
        # if next item is present
        if nextItem:
            nextItem.prevPtr = prevItem
        else:
            self.tail = prevItem
        # make sure head prev is None
        if self.head:
            self.head.prevPtr = None
        # make sure tail next is None
        if self.tail:
            self.tail.nextPtr = None
        # cleanup
        item.nextPtr = None
        item.prevPtr = None
        # decrement size
        self.capacity -= 1
        return item.key, item.val

    def pop(self) -> CacheItem:
        # if queue is empty return none
        if self.capacity == 0:
            return None

        prevTail = self.tail
        self.tail = prevTail.prevPtr
        if self.tail:
            self.tail.nextPtr = None
        else:
            # only item removed
            self.head = self.tail = None
        # cleanup
        prevTail.prevPtr = None
        # decrement capacity
        self.capacity -= 1
        return prevTail

    def movetohead(self, item: CacheItem) -> CacheItem:
        # removing item
        key, val = self.remove(item)
        # moving to head (head has higher priority)
        return self.appendleft(key, val)

    def size(self) -> int:
        return self.capacity


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cacheq = CacheQueue()
        self.mem: dict[int, CacheItem] = {}

    def get(self, key: int) -> int:
        if key in self.mem:
            item = self.mem[key]
            # recently accessed
            self.mem[key] = self.cacheq.movetohead(item)
            return self.mem[key].val
        # else item is not present
        return -1

    def put(self, key: int, val: int) -> None:
        # if new item
        if key not in self.mem:
            # if cacheq size limit reached then pop from tail
            # to create space
            if self.cacheq.size() == self.capacity:
                poppedItem = self.cacheq.pop()
                # delete from map as well
                del self.mem[poppedItem.key]
            # insert item at head
            item = self.cacheq.appendleft(key, val)
            self.mem[item.key] = item
        else:
            item = self.mem[key]
            # update value
            item.val = val
            # recently accessed
            self.mem[key] = self.cacheq.movetohead(item)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)