#User function Template for python3

class alphanumeric:
    def __init__(self,name,count):
        self.name=name
        self.count=count
class Solution:
    def sortedStrings(self,N,A):
        #code here
        
        lookup = {}
        res = []
        for i in A:
            lookup[i]=lookup.get(i,0)+1
            
        # print(lookup)    
        for key in sorted(lookup.keys()):
            item = alphanumeric(key,lookup[key])
            res.append(item)
   
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        a=[]
        for i in range(N):
            x=input()
            a.append(x)
        ob=Solution()
        ans=ob.sortedStrings(N,a)
        for i in ans:
            print(i.name,end=" ")
            print(i.count)
# } Driver Code Ends