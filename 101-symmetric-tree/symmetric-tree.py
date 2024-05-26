# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric(root, root)
        
    def symmetric(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2:
            if root1.val != root2.val:
                return False
            else:
                return self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left)
        else:
            return False
