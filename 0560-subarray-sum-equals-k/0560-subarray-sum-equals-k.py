class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        Sum = 0
        prefix_sum = {0:1}
        for i in range(len(nums)):
            Sum+=nums[i]
            if (Sum-k) in prefix_sum:
                count+=prefix_sum[Sum-k]
            prefix_sum[Sum] = prefix_sum.get(Sum,0)+1
        return count


        