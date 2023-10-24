class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word_end = False
        
class WordDictionary:
    def __init__(self):
        self.root = Node("")
        
    def addWord(self, word: str) -> None:
        curr = self.root
        prev = None
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            curr = curr.children[ch]
        curr.is_word_end = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            if word and len(node.children) == 0:
                return False
            
            for i, ch in enumerate(word):
                if ch not in node.children:
                    if ch != ".":
                        return False
                    for child in node.children.values():
                        if dfs(child, word[i + 1:]):
                            return True
                    return False
                node = node.children[ch]
            return node.is_word_end
            
        return dfs(self.root, word)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)