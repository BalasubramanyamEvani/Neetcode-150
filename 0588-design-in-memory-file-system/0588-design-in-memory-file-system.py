class Node:
    def __init__(self, name: str) -> None:
        self.name = name


class FileNode(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.contents = ""


class DirNode(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.children: dict[str, Node] = {}


class FileSystem:
    def __init__(self, delimiter: str = "/") -> None:
        self.root = DirNode(name="/")
        self.delimiter = delimiter

    def mkdir(self, path: str) -> None:
        parts = path.split(self.delimiter)[1:]
        curr = self.root
        for part in parts:
            if part not in curr.children:
                curr.children[part] = DirNode(name=part)
            curr = curr.children[part]

    def ls(self, path: str) -> list[str]:
        if path == "/":
            parts = [path]
        else:
            parts = path.split(self.delimiter)
        levels = len(parts)
        curr = self.root
        for i in range(1, levels):
            curr = curr.children[parts[i]]
        return sorted(curr.children.keys()) if isinstance(curr, DirNode) else [curr.name]

    def addContentToFile(self, path: str, content: str) -> None:
        parts = path.split(self.delimiter)
        levels = len(parts)
        curr = self.root
        for i in range(1, levels):
            if parts[i] not in curr.children:
                if i == levels - 1:
                    curr.children[parts[i]] = FileNode(parts[i])
                else:
                    curr.children[parts[i]] = DirNode(parts[i])
            curr = curr.children[parts[i]]
        if isinstance(curr, FileNode):
            if curr.contents == "":
                curr.contents = content
            else:
                curr.contents += content

    def readContentFromFile(self, path: str) -> str:
        parts = path.split(self.delimiter)
        levels = len(parts)
        curr = self.root
        for i in range(1, levels):
            curr = curr.children[parts[i]]
        if isinstance(curr, FileNode):
            return curr.contents
        return ""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)