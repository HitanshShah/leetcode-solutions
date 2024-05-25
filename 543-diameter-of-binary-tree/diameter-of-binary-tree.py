# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dia = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.helper(root)
        return self.dia
        
    def helper(self, node):
        if not node:
            return 0
        dist_l = self.helper(node.left)
        dist_r = self.helper(node.right)
        self.dia = max(self.dia, dist_l + dist_r)
        return 1+max(dist_l, dist_r)