# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         for num in nums:
#             index = abs(num)-1
#             if nums[index] > 0:
#                 nums[index]*=-1
#         result = []
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 result.append(i+1)
#         return result
            

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        n = len(nums)
        return [i for i in range(1,n+1) if i not in num_set]