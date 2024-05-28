# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, node, minVal, maxVal):
        if not node:
            return True
        elif minVal < node.val < maxVal:
            return self.helper(node.left, minVal, node.val) and self.helper(node.right, node.val, maxVal)
        else:
            return False