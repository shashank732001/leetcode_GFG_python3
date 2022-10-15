#User function Template for python3
class Solution:
	def NBitBinary(self, N):
		# code here
		
		def Nbit(ones,zeros,n,res,out):
		    
		    if n==0:
		        res.append(out)
		        return
		    
		    if ones>=0:
		        out1 = out
		        out1 = out1+"1"
		        Nbit(ones+1,zeros,n-1,res,out1)
		    
		    if zeros<ones:
		        out2 = out
		        out2 =out2+"0"
		        Nbit(ones,zeros+1,n-1,res,out2)
		        
		    return      
		
		ones = 0
		zeros = 0
		res = []
		out = ""
		Nbit(ones,zeros,N,res,out)
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends