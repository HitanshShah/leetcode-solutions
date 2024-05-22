# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        h1 = self.height(root.left)
        h2 = self.height(root.right)
        if abs(h1-h2) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if root is None:
            return 0
        else:
            return 1+max(self.height(root.left), self.height(root.right))