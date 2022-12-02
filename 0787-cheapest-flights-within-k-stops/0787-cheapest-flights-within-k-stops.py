class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [10e9]*n
        prices[src] = 0
        
        for i in range(k+1):
            temp = prices[:]
            for s,d,p in flights:   #s = source, d = destination, p=price
                
                if prices[s]==10e9:
                    continue
                if p + prices[s]< temp[d]:
                    temp[d] = p+prices[s]
            
            prices = temp
        return -1 if prices[dst] == 10e9 else prices[dst]   
                    
        