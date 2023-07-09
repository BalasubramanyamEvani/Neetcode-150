class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {}
        rank = {}
        nums_set = set(nums)
        
        for num in nums_set:
            parent[num] = num
            rank[num] = 1
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
    
        def union(x, y):
            xparent = find(x)
            yparent = find(y)
            if xparent == yparent:
                return False
            if rank[xparent] > rank[yparent]:
                parent[yparent] = xparent
                rank[xparent] += rank[yparent]
            else:
                parent[xparent] = yparent
                rank[yparent] += rank[xparent]
            return True
        
        for num in nums:
            if num + 1 in nums_set:
                union(num, num + 1)
            if num - 1 in nums_set:
                union(num, num - 1)
        
        return max(rank.values()) if len(rank) > 0 else 0
