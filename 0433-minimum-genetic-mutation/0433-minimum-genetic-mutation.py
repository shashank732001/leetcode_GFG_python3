class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        if end not in bank:
            return -1
        
        if start not in bank:
            bank.append(start)
        
        mut = collections.defaultdict(list)
        
        for gene in bank:
            for j in range(len(gene)):
                pattern = gene[:j]+"*"+gene[j+1:]
                mut[pattern].append(gene)
        
        q = deque([start])
        done = set()
        done.add(start)
        res = 0
        
        while q:
            for i in range(len(q)):
                gene = q.popleft()
                if gene==end:
                    return res
                
                for j in range(len(gene)):
                    pattern = gene[:j]+"*"+gene[j+1:]
                    for next_gene in mut[pattern]:
                        if next_gene not in done:
                            done.add(next_gene)
                            q.append(next_gene)
            res+=1
        return -1    
        
        
        
        
#         def diff(string1,string2):
#             diff_count = 0
            
#             for i in range(len(string1)):
#                 if string1[i]!=string2[i]:
#                     diff_count+=1
#             return diff_count
        
        
#         q = deque([(start,0)])
#         visited = set()
        
        
#         while q:
#             string,change = q.popleft()
#             if string==end:
#                 return change
            
#             visited.add(string)
            
#             for mut in bank:
                
#                 if (mut not in visited) and diff(mut,string)==1:
                    
#                     q.append((mut,change+1))
#         return -1            
                    
            
            
            