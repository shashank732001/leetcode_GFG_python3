# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
#         def preOrder(node,count,Max):
            
#             if not node:
#                 return
            
#             if node.val>=Max:
#                 count[0]+=1
#             Max=max(Max,node.val)
#             preOrder(node.left,count,Max)
#             preOrder(node.right,count,Max)
            
#             return
        
#         Max = root.val
#         count = [0]
#         preOrder(root,count,Max)
#         return count[0]
        
    
        def preOrder(node,maxVal):
            if not node:
                return 0
            
            res = 1 if node.val>=maxVal else 0
            maxVal = max(maxVal,node.val)
            left = preOrder(node.left,maxVal)
            right = preOrder(node.right,maxVal)
            
            return res+left+right
        
        return preOrder(root,root.val)
        