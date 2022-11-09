# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        def nextLargest(arr,n):
	
            res = []
            stack  = []


            for i in range(n-1,-1,-1):

                if not stack:
                    res.append(0)

                elif stack and stack[-1]>arr[i]:
                    res.append(stack[-1])

                else:
                    while stack and stack[-1]<=arr[i]:
                        stack.pop()

                    if stack:
                        res.append(stack[-1])

                    else:
                        res.append(0)
                stack.append(arr[i])		
            return res[::-1]
        
        
        
        
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        # print(arr) 
        return nextLargest(arr,len(arr))