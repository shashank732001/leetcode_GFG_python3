class Node:
    
    def __init__(self,key,val):
        self.key =key
        self.val =val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps key to node
        
        self.left = Node(0,0)  # helps to find least recent used
        
        self.right = Node(0,0)  # helps to find most recently used
        
        self.left.next,self.right.prev = self.right,self.left
    
    
    # removes the node from thee list
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev = prev
        
    
    
    # insert the node at the right before right pointer
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next,nxt.prev=node,node
        node.next = nxt
        node.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  #remove from current pos
            self.insert(self.cache[key])  # move it to pos before right pointer to make it most reecnt
            
            return (self.cache[key]).val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # if already exists we have to remove and put it
            
        self.cache[key] = Node(key,value) 
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            # we have to remove least recent from list and  remove it from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)