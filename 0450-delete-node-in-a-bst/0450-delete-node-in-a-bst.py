# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        if not root:
            return None
        
        if root.val == key:
            
            # no child
            if not root.left and not root.right:
                return None
            
            # only left child
            if root.left and not root.right:
                return root.left
            
            #only right child
            if not root.left and root.right:
                return root.right
            
            #both child exists
            ptr = root.right
            
            while ptr.left:
                ptr = ptr.left
            root.val = ptr.val
            root.right = self.deleteNode(root.right,root.val)
            
            
        
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
            
        if root.val<key:
            root.right = self.deleteNode(root.right,key)
            
        return root    
        
        
        