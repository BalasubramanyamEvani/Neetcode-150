# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            for child in [node.left, node.right]:
                if child:
                    graph[node.val].append(child.val)
                    graph[child.val].append(node.val)
                    q.append(child)
        q = deque([target.val])
        visited = set()
        visited.add(target.val)
        while k > 0:
            batchlen = len(q)
            for _ in range(batchlen):
                node = q.popleft()
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        q.append(child)
            k -= 1
        return list(q)
        