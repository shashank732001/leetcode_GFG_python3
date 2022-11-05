
def countRev (s):
    # your code here
    n = len(s)
    if n%2!=0:
        return -1
    
    
    opened = 0
    closed = 0
  
    for i in s:
        if i =="{":
            opened+=1
        else:
            if opened>0:
                opened-=1
            else:    
                closed+=1
        
    return (opened+1)//2+(closed+1)//2
    
    

            
            

#{ 
 # Driver Code Starts

t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends