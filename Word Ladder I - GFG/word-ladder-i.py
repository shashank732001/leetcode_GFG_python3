import collections
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		#Code here
		
		if targetWord not in wordList:
		    return 0
		
		if startWord not in wordList:
		    wordList.append(startWord)
		
		nei = collections.defaultdict(list)
		
		for word in wordList:
		    for j in range(len(word)):
		        pattern = word[:j]+"*"+word[j+1:]
		        nei[pattern].append(word)
	    
	    q = collections.deque([startWord])
	    visit = set()
	    visit.add(startWord)
	    res = 1
	    
	    while q:
	        for i  in range(len(q)):
	            word = q.popleft()
	            if word==targetWord:
	                return res
	            
	            for j in range(len(word)):
	                pattern = word[:j]+"*"+word[j+1:]
	                for neiword in nei[pattern]:
	                    if neiword not in visit:
	                        visit.add(neiword)
	                        q.append(neiword)
	        res+=1
	    return 0      
	                     


#{ 
 # Driver Code Starts
from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends