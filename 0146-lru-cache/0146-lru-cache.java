class LRUCache {
    class CacheNode {
        public CacheNode prev;
        public int key;
        public int value;
        public CacheNode next;

        public CacheNode(CacheNode prev, int key, int value, CacheNode next) {
            this(key, value);
            this.prev = prev;
            this.next = next;
        }

        public CacheNode(int key, int value) {
            this.key = key;
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }

    class CacheQueue {
        public CacheNode head;
        public CacheNode tail;
        public int size;

        public CacheQueue() {
            this.head = null;
            this.tail = null;
            this.size = 0;
        }

        public CacheNode appendLeft(int key, int val) {
            CacheNode newNode = new CacheNode(key, val);
            if (isEmpty()) {
                this.size += 1;
                this.head = newNode;
                this.tail = newNode;
                return newNode;
            }
            this.size += 1;
            newNode.next = this.head;
            this.head.prev = newNode;
            this.head = newNode;
            return newNode;
        }

        public CacheNode remove(CacheNode node) {
            if (isEmpty() || node == null) {
                return null;
            }
            CacheNode prev = node.prev;
            CacheNode next = node.next;
            if (prev != null) {
                prev.next = next;
            } else {
                this.head = next;
            }
            if (next != null) {
                next.prev = prev;
            } else {
                this.tail = prev;
            }
            if (this.head != null) {
                this.head.prev = null;
            }
            if (this.tail != null) {
                this.tail.next = null;
            }
            this.size -= 1;
            node.prev = null;
            node.next = null;
            return node;
        }

        public CacheNode pop() {
            if (isEmpty()) {
                return null;
            }
            CacheNode tailNode = remove(tail);
            return tailNode;
        }

        public CacheNode moveToHead(CacheNode node) {
            if (isEmpty()) {
                return null;
            }
            CacheNode removedNode = remove(node);
            return appendLeft(removedNode.key, removedNode.value);
        }

        public int length() {
            return this.size;
        }

        public boolean isEmpty() {
            return this.size == 0;
        }
    }

    private Map<Integer, CacheNode> mem;
    private CacheQueue cacheQueue;
    private int capacity;

    public LRUCache(int capacity) {
        this.mem = new HashMap<>();
        this.cacheQueue = new CacheQueue();
        this.capacity = capacity;
    }

    public int get(int key) {
        if (!mem.containsKey(key)) {
            return -1;
        }
        CacheNode node = mem.get(key);
        mem.put(key, cacheQueue.moveToHead(node));
        return mem.get(key).value;
    }

    public void put(int key, int value) {
        if (!mem.containsKey(key)) {
            if (cacheQueue.length() == capacity) {
                CacheNode popped = cacheQueue.pop();
                mem.remove(popped.key);
            }
            mem.put(key, cacheQueue.appendLeft(key, value));
        } else {
            CacheNode node = mem.get(key);
            node.value = value;
            mem.put(key, cacheQueue.moveToHead(node));
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */