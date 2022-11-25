# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        
        def right_view(root,level,max_level):
            if root:
                if max_level[0]<level:
                    res.append(root.val)
                    max_level[0]=level

                right_view(root.right,level+1,max_level)
                right_view(root.left,level+1,max_level)
        
        right_view(root,1,[0])
        return res
        
        
        
        # lookup = defaultdict(list)
        # def dfs(node,height):
        #     if not node:return
        #     lookup[height].append(node.val)
        #     dfs(node.left,height+1)
        #     dfs(node.right,height+1)
        # dfs(root,0)
        # return [v[-1] for k,v in lookup.items()]
    
    
    
#         lookup = defaultdict(int)
#         def dfs(node,height):
#             if not node:return
#             if height not in lookup:
#                 lookup[height]=node.val
            
#             dfs(node.right,height+1)
#             dfs(node.left,height+1)
#         dfs(root,0)
#         return lookup.values()