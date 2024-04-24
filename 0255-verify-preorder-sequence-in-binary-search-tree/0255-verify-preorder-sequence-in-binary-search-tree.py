class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def dfs(index, low, high):
            if index == len(preorder):
                return -1, True
            root = preorder[index]
            # cannot fit the node
            if root < low or root > high:
                return index, False
            # at this point the node at index fits
            # since it passes previous if
            
            # check if next index fits in the left subtree
            j, fits = dfs(index + 1, low, root)
            if j >= 0:
                # check if it fits in the right subtree 
                j, fits = dfs(j, root, high)
            return j, fits
        
        _, fits = dfs(0, -math.inf, math.inf)
        return fits
