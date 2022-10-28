#User function Template for python3


def maxSum(arr,n):
    # code here
    arr.sort()
    l = 0
    r = n-1
    re = []
    Sum = 0
    
    for i in range(n):
        if i%2==0:
            re.append(arr[l])
            l+=1
        else:
            re.append(arr[r])
            r-=1
    # print(re)
    for i in range(1,n):
        Sum+=abs(re[i-1]-re[i])
    Sum+=abs(re[-1]-re[0])    
        
        
    return Sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    # x=list(map(int,input().split()))
    # n=x[0]
    # k=x[1]
    arr = list(map(int,input().split()))
    ans=maxSum(arr,n)
    print(ans)

# } Driver Code Ends