class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        Sum = 0
        remainder_index = {0:-1}
        for i in range(len(nums)):
            Sum+=nums[i]
            remainder = Sum%k
            if remainder in remainder_index:
                if(i-remainder_index[remainder]>1):
                    return True
            else:
                remainder_index[remainder] = i
        return False        