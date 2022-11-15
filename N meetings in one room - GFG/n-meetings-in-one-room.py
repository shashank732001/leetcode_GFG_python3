#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        intervals = []
        for i in range(n):
            intervals.append([start[i],end[i]])
            
        intervals.sort(key = lambda i:i[1])
        
        count = 1
        latestend = intervals[0][1]
        
        for start,end in intervals[1:]:
            if start>latestend:
                latestend=end
                count+=1
            
        return count
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends