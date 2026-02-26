class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Use len(matrix) for standard Python lists
        if not matrix or len(matrix) == 0:
            return []
        
        res = []
        # Use len() to get dimensions for standard lists
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse Right
            for i in range(left, right + 1):
                res.append(matrix[top][i]) # Use matrix[r][c] syntax
            top += 1

            # 2. Traverse Down
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # 3. Traverse Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # 4. Traverse Up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res