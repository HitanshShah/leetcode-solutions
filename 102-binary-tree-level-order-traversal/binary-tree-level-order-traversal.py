# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ans = []
        # if not root:
        #     return ans
        # q1 = deque()
        # q2 = deque()
        # q1.append(root)
        # while q1:
        #     curr_lev = []
        #     while q1:
        #         q2.append(q1.popleft())
        #     while q2:
        #         node = q2.popleft()
        #         if node.left:
        #             q1.append(node.left)
        #         if node.right:
        #             q1.append(node.right)
        #         curr_lev.append(node.val)
        #     # print(curr_lev)
        #     ans.append(curr_lev)
        # return ans
        ans = []
        if not root:
            return ans
        q1 = deque()
        q1.append((root,0))
        curr_lvl = -1
        while q1:
            node, level = q1.popleft()
            if curr_lvl != level:
                ans.append([node.val])
                curr_lvl = level
            else:
                ans[-1].append(node.val)
            if node.left:
                q1.append((node.left, level+1))
            if node.right:
                q1.append((node.right, level+1))
        return ans