from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        # code here
        
        q1 = deque([])
        q2 = deque([])
        
        if not node1 and not node2:
            return 1
        
        if (not node1 and node2) or (node1 and not node2):
            
            return 0
        
        q1.append(node1)
        q2.append(node2)
        
        while True:
            
            n1 = len(q1)
            n2 = len(q2)
            if n1!=n2:
                
                return 0
                
            if not q1:
                break
            
            level_arr1 = []
            level_arr2 = []
            
            while q1:
                
                node_1 = q1.popleft()
                
                if node_1.left:
                    q1.append(node_1.left)
                if node_1.right:
                    q1.append(node_1.right)
                    
                
                node_2 = q2.popleft()
                
                if node_2.left:
                    q2.append(node_2.left)
                if node_2.right:
                    q2.append(node_2.right)
                    
                level_arr1.append(node_1.data)
                level_arr2.append(node_2.data)
                
            level_arr1.sort()
            level_arr2.sort()
                
            if level_arr1!=level_arr2:
            
                return 0
        
        return 1            
            
            
        



#{ 
 # Driver Code Starts
class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        node1 = inputTree();
        
        
        node2 = inputTree();
        
        obj = Solution()
        res = obj.areAnagrams(node1, node2)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends