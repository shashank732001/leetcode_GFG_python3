class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won = []
        lost = []
        
        win_lookup = {}
        lose_lookup = {}
        
        for player1,player2 in matches:
            
            win_lookup[player1] = 1+win_lookup.get(player1,0)
            lose_lookup[player2] = 1+lose_lookup.get(player2,0)
            
        for key, val in win_lookup.items():
            if key not in lose_lookup:
                won.append(key)
        
        for key,val in lose_lookup.items():
            if val==1:
                lost.append(key)
        won.sort()
        lost.sort()
        return [won,lost]        
        