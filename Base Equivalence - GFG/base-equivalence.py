#User function Template for python3
class Solution:
	def baseEquiv(self, n, m):
		# code here
		
# 		flag = False
		
		for i in range(2,33):
		    
		    count = 0
		    temp = n
		    
		    for j in range(m):
		        if not temp:break
		        
		        temp = int(temp/i)
		        count+=1
		        
		        if temp==0 and count==m:
		            return "Yes"
		            
	    return "No"	            
		        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n=int(n)
		m=int(m)
		ob = Solution();
		print(ob.baseEquiv(n,m))

# } Driver Code Ends