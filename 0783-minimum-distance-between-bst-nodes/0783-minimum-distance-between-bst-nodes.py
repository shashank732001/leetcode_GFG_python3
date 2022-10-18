# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

    
    
        def inorder(node,prev,ans):
            if not node:
                return 
            
            inorder(node.left,prev,ans)
            if prev[0]:
                ans[0] = min(ans[0],abs(node.val-prev[0].val))
            
            prev[0] = node
            inorder(node.right,prev,ans)
        
        prev = [None]
        ans = [10e9]
        inorder(root,prev,ans)
        return ans[0]