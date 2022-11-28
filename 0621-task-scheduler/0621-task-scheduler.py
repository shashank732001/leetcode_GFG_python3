class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque() # [-cnt,pairs]
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time  = 0
        
        while q or maxHeap:
            time+=1
            
            if maxHeap:
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                cnt,idletime = q.popleft()
                heapq.heappush(maxHeap,cnt)
        return time        
                