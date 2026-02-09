class Solution:
    def sortedSquares(self, nums: list[int]) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        result = [0]*n
        for i in range(n-1,-1,-1):
            if abs(nums[l]) > abs(nums[r]):
                result[i] = nums[l]**2
                l+=1
            else:
                result[i] = nums[r]**2
                r-=1
        return result



        