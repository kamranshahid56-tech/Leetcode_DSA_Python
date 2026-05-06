class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_set = set()
        l = 0
        maxSum = 0
        currentSum = 0
        
        for r in range(len(nums)):
            # 1. Handle Duplicates: 
            # Slide 'l' until the duplicate of nums[r] is gone
            while nums[r] in num_set:
                num_set.remove(nums[l])
                currentSum -= nums[l]
                l += 1
            
            # 2. Add current element
            num_set.add(nums[r])
            currentSum += nums[r]
            
            # 3. Handle Size: 
            # If window is now larger than k, remove exactly ONE element from left
            if (r - l + 1) > k:
                num_set.remove(nums[l])
                currentSum -= nums[l]
                l += 1
            
            # 4. Success Condition:
            # If we have exactly k elements and they are all distinct
            if (r - l + 1) == k:
                maxSum = max(maxSum, currentSum)
                
        return maxSum