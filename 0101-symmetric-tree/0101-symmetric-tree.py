# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """DFS Recursive solution"""
#         def sym(nodeleft,noderight):
#             if nodeleft and noderight and nodeleft.val==noderight.val:
#                 return sym(nodeleft.right,noderight.left) and sym(nodeleft.left,noderight.right)

            
#             return not nodeleft and not noderight
               
            
#         return sym(root.left,root.right)  


        """BFS solution"""
        

        leftq = deque([root.left])
        rightq = deque([root.right])

        while leftq and rightq:
            nodeleft = leftq.popleft()
            noderight= rightq.popleft()

            if nodeleft and noderight:
                if nodeleft.val!=noderight.val:
                    return False

                leftq.append(nodeleft.left)
                leftq.append(nodeleft.right)
                rightq.append(noderight.right)
                rightq.append(noderight.left)

            elif nodeleft or noderight:
                return False
        return not leftq and not rightq    
                