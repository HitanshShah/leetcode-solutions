# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q1 = deque()
        q2 = deque()
        q1.append(root)
        while q1:
            curr_lev = []
            while q1:
                q2.append(q1.popleft())
            while q2:
                node = q2.popleft()
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
                curr_lev.append(node.val)
            # print(curr_lev)
            ans.append(curr_lev)
        return ans