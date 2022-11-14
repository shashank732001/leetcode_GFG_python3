# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def search(node,ans):
            if not node:
                return "N"
            if node:
                curr = str(node.val)
            else:
                curr = ""
            s = search(node.left,ans)+"-->"+search(node.right,ans)+"-->"+curr
            lookup[s] = lookup.get(s,0)+1
            
            if lookup[s]==2 :
                ans.append(node)
            return s    
        if not root:
            return [[0]]
        lookup = {}
        ans = []
        search(root,ans)
        return ans