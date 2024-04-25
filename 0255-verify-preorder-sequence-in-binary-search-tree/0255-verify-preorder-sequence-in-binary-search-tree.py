class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # Brute Force
#         def dfs(l, r):
#             if l > r:
#                 return True
#             root = preorder[l]
#             i = l + 1
#             # finding left ST contents valid
#             while i <= r and preorder[i] < root:
#                 i += 1
#             if not dfs(l + 1, i - 1):
#                 return False
#             #finding right ST contents valid
#             j = i
#             while j <= r and preorder[j] > root:
#                 j += 1
#             if j != r + 1 or not dfs(i, r):
#                 return False
#             return True
        
#         N = len(preorder)
#         return dfs(0, N - 1)

            # recursive
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
        
        # monotonic stack
        # by default appending to stack is appending to left subtree
        # when we can no longer append to left ST, then pop from top
        # and change limits and see if it can fit in right ST
        # stack = []
        # cur = [-math.inf, math.inf]
        # for num in preorder:
        #     while stack and stack[-1][0] < num:
        #         temp = stack.pop()
        #         cur[0] = temp[0]
        #         cur[1] = temp[2]
        #     if not cur[0] < num < cur[1]:
        #         return False
        #     stack.append((num, *cur))
        #     cur[1] = num
        # return True
