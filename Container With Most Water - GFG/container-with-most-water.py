#User function Template for python3



def maxArea(A,le):
    #code here
    l = 0
    r = le-1
    area = 0
    
    while l<r:
        area = max(area,min(A[l],A[r])*(r-l))
        
        if A[l]>=A[r]:
            r-=1
        else:
            l+=1
    return area        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends