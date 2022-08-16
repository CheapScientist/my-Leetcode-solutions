// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        build = []
        
        def dfs(node):
            if not node: return
            build.append(str(node.val))
            if (not node.left) and (not node.right): 
                ans.append('->'.join(build))
            dfs(node.left)
            dfs(node.right)
            build.pop()
            
            
        dfs(root)
        return ans
                