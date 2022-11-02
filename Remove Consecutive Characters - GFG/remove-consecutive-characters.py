#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        i = 0
        S = list(S)
        while i<len(S)-1:
            if S[i]==S[i+1]:
                S.pop(i)
            else:
                i+=1
        return "".join(S)        
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends