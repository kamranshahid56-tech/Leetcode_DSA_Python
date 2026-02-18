class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0]*(n+1)
        for x in nums:
            counts[x]+=1
        
        duplicate = -1
        missing = -1
        for i in range(1,n+1):
            if counts[i] == 2:
                duplicate = i
            elif counts[i] == 0:
                missing = i
        return [duplicate, missing]

