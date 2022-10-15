#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        S = list(S)
        ans = []
        index = 0
        self.solve(S,ans,index)
        ans.sort()
        return ans  
    
    def solve(self,S,ans,index):
            if index>=len(S):
                output = "".join(S)
                if output not in ans:
                    ans.append(output)
                return set(ans)
            
            for i in range(index,len(S)):
                S[index],S[i] = S[i],S[index]
                self.solve(S,ans,index+1)
                S[index],S[i] = S[i],S[index]    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends