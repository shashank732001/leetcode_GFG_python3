#User function Template for python3


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here
        # res = []
        
        # def in_order(root):
            
        #     if not root:return              # this is the recursive way
        #     in_order(root.left)
        #     res.append(root.data)
        #     in_order(root.right)
        
        # in_order(root)
        # return res
        
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)               # this is the itearative way
                curr =curr.left
            curr = stack.pop()    
            res.append(curr.data)
            curr = curr.right
        return res    
            


"""
Inorder  = left-->root-->right
Preorder  = root-->left-->right
Postorder  = left-->right-->root


Now we can solve this problem in two ways 
1.Recursively     Time-->O(n)   Space  -->O(n)
2.iteratively
"""
#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = Solution().InOrder(root)
        for i in range (len(res)):
            print (res[i], end = " ")
        print()
        
        

# } Driver Code Ends