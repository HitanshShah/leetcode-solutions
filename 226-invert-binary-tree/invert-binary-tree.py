# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invert(root)
        return root
        
    
    def invert(self, root):
        if not root.left and not root.right:
            return root
        else:
            temp = TreeNode()
            temp = root.left
            root.left = root.right
            root.right = temp
            if root.left:
                root.left = self.invert(root.left)
            if root.right:
                root.right = self.invert(root.right)
            return root