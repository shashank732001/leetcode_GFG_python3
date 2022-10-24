class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l,r=0,0
        s=""
        res=0
        def knapsack(path,arr,index):
            a,b=len(path),len(Counter(path))
            if a==b:
                nonlocal res
                res=max(res,len(path))
            elif a!=b:
                return
            if index>=len(arr):return
            knapsack(path+arr[index],arr,index+1)
            knapsack(path,arr,index+1)
        knapsack("",arr,0)
        return res            