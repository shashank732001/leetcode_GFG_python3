class Solution:
    def numSquares(self, n: int) -> int:
        dp = [ 10e9 for _ in range(n+1) ]
        dp[0] = 0
        
        ini = 1
        square = ini*ini
        
        # for each square number 1, 4, 9, 16, 25...
        while( square <= n ) :
            
            # update dp value for number from square to n
            for i in range(square, n+1) :
                
                dp[i] = min( dp[i], dp[i-square]+1 )
            
            # go to next square number
            ini += 1
            square = ini*ini
        
        
        return dp[n]