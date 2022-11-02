class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def diff(string1,string2):
            diff_count = 0
            
            for i in range(len(string1)):
                if string1[i]!=string2[i]:
                    diff_count+=1
            return diff_count
        
        
        q = deque([(start,0)])
        visited = set()
        
        
        while q:
            string,change = q.popleft()
            if string==end:
                return change
            
            visited.add(string)
            
            for mut in bank:
                
                if (mut not in visited) and diff(mut,string)==1:
                    
                    q.append((mut,change+1))
        return -1            
                    
            
            
            