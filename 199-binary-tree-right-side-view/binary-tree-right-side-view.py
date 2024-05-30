# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        self.helper(ans, root, 0)
        return ans
        
    def helper(self, ans, root, currLevel):
        if currLevel == len(ans):
            ans.append(root.val)
        if root.right:
            self.helper(ans, root.right, currLevel+1)
        if root.left:
            self.helper(ans, root.left, currLevel+1)
        return