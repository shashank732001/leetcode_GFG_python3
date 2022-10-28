#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        # n0, n1, n2 = -1, -1, -1
        # for num in arr:
        #     if num == 0:
        #         n2 += 1
        #         arr[n2] = 2
        #         n1 += 1
        #         arr[n1] = 1
        #         n0 += 1
        #         arr[n0] = 0
        #     elif num == 1:
        #         n2 += 1
        #         arr[n2] = 2
        #         n1 += 1
        #         arr[n1] = 1
        #     elif num == 2:
        #         n2 += 1
        #         arr[n2] = 2
        
        
        i,j,k=0,0,n-1
        """
        two pointers for either end and 1 pointer to check the value
        here i will be at left end 
         and k will be at right end
         j will be the iterator
        """
        
        while j<=k:
            if arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j+=1
            elif arr[j]==1:
                j+=1
            else:
                arr[j],arr[k]=arr[k],arr[j]
                k-=1
        return arr        
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends