import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        n = len(matrix)

        for r in range(min(n,k)):
            heapq.heappush(min_heap,(matrix[r][0],r,0))
        
        for _ in range(k-1):
            val,r,c = heapq.heappop(min_heap)
        
            if c+1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1],r,c+1))

        return min_heap[0][0]