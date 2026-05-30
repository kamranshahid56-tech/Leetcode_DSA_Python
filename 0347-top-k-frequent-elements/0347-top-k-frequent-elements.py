import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Build the frequency map
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        min_heap = []
        for num, freq in num_map.items():
            heapq.heappush(min_heap,(freq, num))
        
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        return [num for freq,num in min_heap]

        