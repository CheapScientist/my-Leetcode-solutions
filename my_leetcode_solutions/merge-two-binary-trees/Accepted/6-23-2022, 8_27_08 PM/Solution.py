// https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(p, q):
            if not p and not q: return None
            new = TreeNode()
            if p and not q: 
                new.val = p.val
                left = dfs(p.left, None)
                right = dfs(p.right, None)
                new.left, new.right = left, right
                return new
            elif q and not p: 
                new.val = q.val
                left = dfs(None, q.left)
                right = dfs(None, q.right)
                new.left, new.right = left, right
                return new
            else: 
                new.val = p.val + q.val
                left, right = dfs(p.left, q.left), dfs(p.right, q.right)
                new.left, new.right = left, right 
                return new
        return dfs(root1, root2)