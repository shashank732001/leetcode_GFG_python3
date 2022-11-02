class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def check(a,b):
            c=0
            for x in range(len(a)):
                if a[x]!=b[x]:
                    c+=1
            return c
        visited=set()
        l=deque([(start,0)])
        flag=0
        while l:
            t,count=l.popleft()
            if t==end:
                return count
            visited.add(t)
            for x in bank:
                #print(check(t,x))
                if x not in visited and check(t,x)==1:
                    l.append([x,count+1])
            #print(l)
        return -1