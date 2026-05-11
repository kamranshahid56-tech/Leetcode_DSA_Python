class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = m*n-1
        while l<=h:
            mid = h-l//2
            row = mid//n
            column = mid%n
            if(target == matrix[row][column]):
                return True
            elif (target <= matrix[row][column]):
                h = mid-1
            else:
                l = mid+1
        return False
