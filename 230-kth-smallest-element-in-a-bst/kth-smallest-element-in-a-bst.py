# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        self.inOrder(root, traversal)
        return traversal[k-1]

    def inOrder(self, root, traversal):
        if not root:
            return
        self.inOrder(root.left, traversal)
        traversal.append(root.val)
        self.inOrder(root.right, traversal)
        return