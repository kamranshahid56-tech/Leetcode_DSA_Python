class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum+=num
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum-left_sum-nums[i]
            if (left_sum == right_sum):
                return i
            left_sum+=nums[i]
        return -1
        