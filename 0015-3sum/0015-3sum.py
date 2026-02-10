class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # 1. Skip duplicates for the fixed number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 2. Optimization: If the smallest possible sum is > 0, stop everything
            # (Because the list is sorted, all following numbers are even larger)
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            
            # 3. Optimization: If the largest possible sum for this 'i' is < 0, 
            # this 'i' is too small, move to the next 'i'
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
                
            l, r = i + 1, n - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 4. Skip duplicates for BOTH pointers to shrink window faster
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                        
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
                    
        return result
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result = []
#         for i in range(len(nums)-2):
#             if i>0 and nums[i] == nums[i-1]:
#                 continue
#             l,r = i+1,len(nums)-1
#             while l < r:
#                 three_sum = nums[l]+nums[r]+nums[i]
#                 if three_sum == 0:
#                     result.append([nums[l],nums[r],nums[i]])
#                     l+=1
#                     r-=1
#                     while l<r and nums[l] == nums[l-1]:
#                         l+=1
#                 elif three_sum < 0:
#                     l+=1
#                 else:
#                     r-=1
#         return result
                