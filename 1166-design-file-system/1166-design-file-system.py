class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = {}

class FileSystem:

    def __init__(self):
        self._trie = Node("/", -1)

    def createPath(self, path: str, value: int) -> bool:
        components = path.split("/")
        if not self._check_valid(components):
            return False
        curr = self._trie
        start = 0 if components[0] else 1
        for i in range(1, len(components)):
            if i == len(components) - 1:
                break
            part = components[i]
            if part not in curr.children:
                return False
            curr = curr.children[part]
        if components[-1] in curr.children:
            return False
        curr.children[components[-1]] = Node(components[-1], value)
        return True

    def get(self, path: str) -> int:
        components = path.split("/")
        if not self._check_valid(components):
            return -1
        curr = self._trie
        start = 0 if components[0] else 1
        for i in range(1, len(components)):
            part = components[i]
            if part not in curr.children:
                return -1
            curr = curr.children[part]
        return curr.value

    def _check_valid(self, components: list[str]) -> bool:
        for i, part in enumerate(components):
            if i > 0 and not part:
                return False
        return True

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)