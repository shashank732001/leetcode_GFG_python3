#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        lst =[]
        def merge_sort(arr):
        	if len(arr)>1:
        		left_arr =arr[:len(arr)//2]           #divide into two parts 
        		right_arr = arr[len(arr)//2:]
        
        		merge_sort(left_arr)
        		merge_sort(right_arr)                  # divide again till array size is 1
        
        
        		i = 0
        		j = 0 
        		k = 0
        
        		while i<len(left_arr) and j<len(right_arr):    #making sure arr is not empty
        
        			if left_arr[i]<right_arr[j]:                 #comparing leftmost element of both arr
        				arr[k] = left_arr[i]
        				i+=1
        			else:
        				arr[k]=right_arr[j]
        				j+=1
        			k+=1
        			
        
        		while i<len(left_arr):
        			arr[k] = left_arr[i]
        			i+=1
        			k+=1
        
        		while j<len(right_arr):
        			arr[k]=right_arr[j]
        			j+=1
        			k+=1
        			
        while head:
            lst.append(head.data)
            head=head.next
        merge_sort(lst)    
        # print(lst) 
        
        curr = Node(0)
        dummy = curr
        
        for i in lst:
            curr.next = Node(i)
            curr = curr.next
        return dummy.next    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends