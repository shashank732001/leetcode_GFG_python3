#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

# Function to delete a given node from the list 
def deleteNode(head, key):
    #your code goes here
    curr = head
    my_prev = None
    
    while curr.data!=key:
        my_prev = curr
        curr = curr.next
    my_prev.next = curr.next
    curr.next = None
    return head
    


#Function to reverse the list
def reverse(head):
    #your code goes here
    # my_prev = None
    # curr = head
    # my_head = head
    # while curr:
    #     temp = curr.next
    #     curr.next = my_prev
    #     my_prev,curr = curr,temp
      
    # return my_head
    
    t = head
    a = []
    while t.next != head:
        a.append(t.data)
        t = t.next
    a.append(t.data)
    
    c = head
    for i in a[::-1]:
        c.data = i
        c = c.next



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(data, prev):
    if prev == None:
        prev = Node(data)
        return prev
    tmp = Node(data)
    prev.next = tmp
    return tmp

def printList(head):
    flg = False
    tmp = head
    while flg== False or tmp!=head:
        flg = True
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        delNode = int(input())

        head = Node(None)
        prev = head
        for i in arr:
            prev = push(i, prev)
        head = head.next
        prev.next = head
        deleteNode(head, delNode)
        reverse(head)
        printList(head)

# } Driver Code Ends