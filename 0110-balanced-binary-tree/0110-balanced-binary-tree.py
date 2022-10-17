# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [0]
        
        def helper(node):
            
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            res[0] = max(res[0],abs(left-right))
            
            return 1+max(left,right)
        
        helper(root)
        return False if res[0]>1 else True
            