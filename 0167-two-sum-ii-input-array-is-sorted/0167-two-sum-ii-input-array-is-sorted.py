class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0,n-1
        while l<r:
            Sum = numbers[l]+numbers[r]
            if Sum == target:
                return [l+1,r+1]
            elif Sum < target:
                l+=1
            elif Sum > target:
                r-=1
            else:
                return -1
            
