class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		Intervals.sort(key=lambda x:x[0])
        n=len(Intervals)
        j=0
        i=1
       
        while i<n:
           
            if Intervals[j][1]>=Intervals[i][0]:
                Intervals[j][0]=min(Intervals[j][0],Intervals[i][0])
                Intervals[j][1]=max(Intervals[j][1],Intervals[i][1])
                Intervals.pop(i)
               #i+=1
                n-=1
            else:
                i+=1
                j+=1
        return Intervals     
		    
		    


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends