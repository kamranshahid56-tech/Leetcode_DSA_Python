# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        if root == None:
            return arr
        queue = deque([root])
        isForward = True
        while queue:
            n = len(queue)
            arr1 = []
            for i in range(n):
                curr = queue.popleft()
                if isForward:
                    arr1.append(curr.val)  # Standard append (adds to end)
                else:
                    arr1.insert(0, curr.val)  # Standard insert at index 0 (adds to front)
                if (curr.left is not None):
                    queue.append(curr.left)
                if (curr.right is not None):
                    queue.append(curr.right)
            arr.append(arr1)
            isForward = not isForward
        return arr

        