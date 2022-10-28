#User function Template for python3


def find(arr,n,x):
    # code here
    first,last = -1,-1
    l = 0
    r = n-1
    
    # while l<=r:
    #     if arr[l]!=x:
    #         l+=1
    #     else:
    #         first = l
    #         if arr[r]==x:
    #             last = r
    #             break
    #         else:
    #             r-=1
    # return first,last          
    
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==x:
            while l<=mid:
                if arr[l]==x:
                    first = l
                    break
                l+=1
            while r>=mid:
                if arr[r]==x:
                    last = r
                    break
                r-=1
            break    
        
        elif arr[mid]>x:
            r = mid-1
            
        else:
            l = mid+1
    return first,last        
                



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends