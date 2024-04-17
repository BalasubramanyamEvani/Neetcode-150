class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        A = sorted(nums1)
        B = sorted(nums2)
        N, M = len(A), len(B)
        
        heap = []
        heapq.heappush(heap, (A[0] + B[0], 0, 0))
        
        visited = set()
        visited.add((0, 0))
        
        ret = []
        while heap and k > 0:
            csum, i, j = heapq.heappop(heap)
            ret.append([nums1[i], nums2[j]])
            
            if i + 1 < N and (i + 1, j) not in visited:
                heapq.heappush(heap, (A[i + 1] + B[j], i + 1, j))
                visited.add((i + 1, j))
            
            if j + 1 < M and (i, j + 1) not in visited:
                heapq.heappush(heap, (A[i] + B[j + 1], i, j + 1))
                visited.add((i, j + 1))
            k -= 1

        return ret
