# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque([root])
        
        # Track the absolute maximum sum and its corresponding level
        max_sum = float('-inf')  # Start at negative infinity to handle negative node values
        max_level = 1
        current_level = 1
        
        while queue:
            level_size = len(queue)
            level_sum = 0  # Reset sum for the current level
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Push children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update the max sum and level if we found a strictly greater sum
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            # Move to the next level index
            current_level += 1
            
        return max_level
        