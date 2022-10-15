#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		
		def subs(inp,out,res):
		    
		    if len(inp)==0:
		        res.append(out)
		        return
		    
		    out1 = out[:]
		    out2 = out[:]
		    out2 = out2+inp[0]
		  #  print(out2)
		    subs(inp[1:],out1,res)
		    subs(inp[1:],out2,res)
		    return
		
		res = []
		out = ""
		subs(s,out,res)
		return sorted(res[1:])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends