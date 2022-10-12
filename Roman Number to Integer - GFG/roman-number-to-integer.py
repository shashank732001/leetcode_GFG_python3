#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        rom = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        res = 0
        
        for i in range(len(S)):
            if i+1<len(S) and rom[S[i]]<rom[S[i+1]]:
                res-=rom[S[i]]
            else:
                res+=rom[S[i]]
        return  res      


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends