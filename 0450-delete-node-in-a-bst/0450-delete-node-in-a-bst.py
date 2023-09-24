# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val
        
    def get_successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left:
                pred = self.get_predecessor(root)
                root.val = pred
                root.left = self.deleteNode(root.left, pred)
            elif root.right:
                suc = self.get_successor(root)
                root.val = suc
                root.right = self.deleteNode(root.right, suc)
            else:
                return None
        return root
                
                
                
        