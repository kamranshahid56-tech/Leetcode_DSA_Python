# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        pq = deque([root])
        pq.append(root)
        depth = 1
        while pq:
            size = len(pq)
            for i in range(size):
                node = pq.popleft()
                if(node.left == None and node.right == None):
                    return depth
                
                if(node.left is not None):
                    pq.append(node.left)
                if(node.right is not None):
                    pq.append(node.right)

            depth+=1
        return depth

        