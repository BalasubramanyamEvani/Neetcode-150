# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:    
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def calc_height(node):
            if not node:
                return 0
            return max(1 + calc_height(node.left), 1 + calc_height(node.right))
        q = deque([root])
        ret = []
        i = 0
        tree_height = calc_height(root)
        num_elements = math.pow(2, tree_height) - 1
        while q and i < num_elements:
            node = q.popleft()
            if node:
                ret.append(str(node.val))
            else:
                ret.append("n")
            if node:
                q.append(node.left)
                q.append(node.right)
            i += 1
        encoded = ":".join(ret)
        return encoded

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        nodes = data.split(":")
        N = len(nodes)
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while i < N:
            curr = q.popleft()
            lval = TreeNode(int(nodes[i])) if nodes[i] != "n" else None
            rval = TreeNode(int(nodes[i + 1])) if nodes[i + 1] != "n" else None
            curr.left = lval
            curr.right = rval
            if lval:
                q.append(lval)
            if rval:
                q.append(rval)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))