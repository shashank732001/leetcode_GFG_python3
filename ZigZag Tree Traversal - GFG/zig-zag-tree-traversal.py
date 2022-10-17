#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Your code here
        s1 = [root]     #array for nodes at odd level
        s2 = []         #array for nodes at even level
        res = []
        
        if not root:
            return res
        
        while s1 or s2:
            while s1:
                node = s1.pop()
                res.append(node.data)
                if node.left:                   # first we are adding left because we pop from last(i,e right nodes first) so observe at even level we want move from right to left 
                    s2.append(node.left)
                    
                if node.right:
                    s2.append(node.right)

            while s2:
                node = s2.pop()
                res.append(node.data)
                
                if node.right:               ## first we are adding right because we pop from last(i,e left nodes first) so observe at odd level we want move from left o right
                    s1.append(node.right)
                    
                if node.left:
                    s1.append(node.left)
        return res        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

from collections import defaultdict
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
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
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.zigZagTraversal(root)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends