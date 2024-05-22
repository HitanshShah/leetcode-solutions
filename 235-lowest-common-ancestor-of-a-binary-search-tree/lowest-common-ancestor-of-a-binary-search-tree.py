# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p.val == root.val or q.val == root.val:
        #     return root
        # elif (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
        #     return root
        # elif p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)
        foundp = False
        foundq = False
        root_p, root_q = root, root
        ancestor = root
        while (root_p and not foundp) and (root_q and not foundq):
            if not foundp:
                if p.val == root_p.val:
                    foundp = True
                elif p.val < root_p.val:
                    root_p = root_p.left
                else:
                    root_p = root_p.right
            if not foundq:
                if q.val == root_q.val:
                    foundq = True
                elif q.val < root_q.val:
                    root_q = root_q.left
                else:
                    root_q = root_q.right
            if root_p.val == root_q.val:
                ancestor = root_p
        return ancestor