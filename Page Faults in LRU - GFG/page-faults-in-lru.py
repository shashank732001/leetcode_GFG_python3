#User function Template for python3

class Solution:
    def pageFaults(self, N, C, pages):
        # code here
        LRU = []
        fault = 0
        
        for i in pages:
            if i not in LRU:
                
                if len(LRU)<C:
                    LRU.append(i)
                else:
                    LRU.pop(0)
                    LRU.append(i)
                fault+=1    
            else:
                LRU.remove(i)
                LRU.append(i)
        return fault        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        pages = input().split()
        for itr in range(N):
            pages[itr] = int(pages[itr])
        C = int(input())

        ob = Solution()
        print(ob.pageFaults(N, C, pages))

# } Driver Code Ends