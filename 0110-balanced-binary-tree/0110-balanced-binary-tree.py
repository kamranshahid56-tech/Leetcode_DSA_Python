# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return  self.checkHeight(root)

    def checkHeight(self,root):
        if root == None:
            return True
        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)

        if abs(leftHeight - rightHeight)>1:
            return False
            
        return self.checkHeight(root.left) and self.checkHeight(root.right)

    def findHeight(self,node):
        if node == None:
            return 0
            
        left = self.findHeight(node.left)
        right = self.findHeight(node.right)

        return 1+max(left,right)
        