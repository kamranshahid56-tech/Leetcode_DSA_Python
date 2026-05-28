# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        if root == None:
            return arr
        queue = deque([root])
        while queue:
            n = len(queue)
            arr1 = []
            for i in range(n):
                curr = queue.popleft()
                arr1.append(curr.val)

                if (curr.left is not None):
                    queue.append(curr.left)
                if (curr.right is not None):
                    queue.append(curr.right)
            arr.append(arr1)
        return arr

        