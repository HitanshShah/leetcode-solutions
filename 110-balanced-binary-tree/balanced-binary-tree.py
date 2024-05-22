# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return True, 0
        left_bal, left_height = self.helper(root.left)
        if not left_bal:
            return False, 0
        right_bal, right_height = self.helper(root.right)
        if not right_bal:
            return False, 0
        return abs(left_height - right_height) < 2, 1+max(left_height, right_height)