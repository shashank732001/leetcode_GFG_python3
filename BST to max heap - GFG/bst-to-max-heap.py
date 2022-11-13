#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def convertToMaxHeapUtil(self, root):
        #code here
        def inorderTraversal(root, arr):
            if root == None:
                return
         
            # first recur on left subtree
            inorderTraversal(root.left, arr)
         
            # then copy the data of the node
            arr.append(root.data)
         
            # now recur for right subtree
            inorderTraversal(root.right, arr)
 
        # function to convert the given
        # BST to MIN HEAP performs preorder
        # traversal of the tree
 
 
        def BSTToMinHeap(root, arr, i):
            if root == None:
                return
         
            # first copy data at index 'i' of
            # 'arr' to the node
            

            # then recur on left subtree
            BSTToMinHeap(root.left, arr, i)
            
            # now recur on right subtree
            BSTToMinHeap(root.right, arr, i)
         
            i[0] += 1
            root.data = arr[i[0]]
        # utility function to convert the
        # given BST to MIN HEAP
         
         
    
        arr = []
        i = [-1]
         
        # inorder traversal to populate 'arr'
        inorderTraversal(root, arr)
         
        # BST to MIN HEAP conversion
        BSTToMinHeap(root, arr, i)    


#{ 
 # Driver Code Starts
# Initial Template for Python

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
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
    
def postOrder(root):
    if root==None:
        return 
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        ob.convertToMaxHeapUtil(root)
        postOrder(root)
            
        print()
        
        

# } Driver Code Ends