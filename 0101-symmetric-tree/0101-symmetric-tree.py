# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def sym(nodeleft,noderight):
            if nodeleft and noderight and nodeleft.val==noderight.val:
                return sym(nodeleft.right,noderight.left) and sym(nodeleft.left,noderight.right)

            
            return not nodeleft and not noderight
               
            
        return sym(root.left,root.right)    
                