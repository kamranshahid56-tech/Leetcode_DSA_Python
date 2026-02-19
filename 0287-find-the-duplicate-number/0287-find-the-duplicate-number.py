class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        counts = [0]*(n+1)
        for x in nums:
            counts[x]+=1
        
        duplicate = -1
        for i in range(1,n+1):
            if counts[i] > 1:
                duplicate = i
            else:
                continue
        return duplicate
        