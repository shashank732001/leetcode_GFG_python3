#User function Template for python3

# design the class in the most optimal way

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.cap = cap
        self.cache = {} # maps key to node
        
        self.left = Node(0,0) #helps to find least recent used
        self.right = Node(0,0) #helps to find most recently used
        
        self.left.next,self.right.prev=self.right,self.left
    
    #  this helps to remove a node from the list
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next = nxt
        nxt.prev = prev
    
    
    # this helps to insert the node at pos just before right pointer
    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next,nxt.prev = node,node
        node.next =nxt
        node.prev = prev
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return (self.cache[key]).val
        return -1    
        
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        #code here
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            #we have to remove the lru from list as well as cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends