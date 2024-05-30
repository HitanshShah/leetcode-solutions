# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     ans = []
    #     if not root:
    #         return ans
    #     self.helper(ans, root, 0)
    #     return ans
        
    # def helper(self, ans, root, currLevel):
    #     if currLevel == len(ans):
    #         ans.append(root.val)
    #     if root.right:
    #         self.helper(ans, root.right, currLevel+1)
    #     if root.left:
    #         self.helper(ans, root.left, currLevel+1)
    #     return
        ans = []
        if not root:
            return ans
        queue = deque()
        queue.append((root,0))
        while queue:
            node, lvl = queue.popleft()
            if lvl == len(ans):
                ans.append(node.val)
            if node.right:
                queue.append((node.right, lvl+1))
            if node.left:
                queue.append((node.left, lvl+1))
        return ans