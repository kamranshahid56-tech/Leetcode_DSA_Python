class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        total_sum = 0
        for r in range(len(nums)):
            total_sum+=nums[r]
        for i in range(len(nums)):
            right_sum = total_sum-left_sum-nums[i]
            if left_sum == right_sum:
                return i
            left_sum+=nums[i]
        return -1 
        
        