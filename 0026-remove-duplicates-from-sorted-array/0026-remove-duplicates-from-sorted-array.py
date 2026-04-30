class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_map = {}
        for n in nums:
            num_map[n] = True
        
        unique_keys = list(num_map.keys())
        for i in range(len(unique_keys)):
            nums[i] = unique_keys[i]
        
        return len(unique_keys)

        