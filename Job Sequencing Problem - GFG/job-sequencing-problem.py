#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        arr = []
        Max_deadline = 0
        for i in Jobs:
            arr.append([i.id,i.deadline,i.profit])
            Max_deadline = max(Max_deadline,i.deadline)
        # print(arr)
        arr.sort(key = lambda i :i[2],reverse = True)
        # print(arr)
        
        slots = [-1]*(Max_deadline+1)
        count=0
        Max_profit = 0
        
        for i in range(n):
            
            for j in range(arr[i][1],0,-1):
                
                if slots[j]==-1:
                    count+=1
                    Max_profit+=arr[i][2]
                    slots[j]=i
                    break
        return [count,Max_profit]        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends