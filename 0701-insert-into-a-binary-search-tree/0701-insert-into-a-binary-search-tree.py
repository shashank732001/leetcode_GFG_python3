# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def insert(node):
            
            if val>node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right)
            
            
            else:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left)
        
        if not root:
            return TreeNode(val)
        
        
        insert(root)
        return root
            