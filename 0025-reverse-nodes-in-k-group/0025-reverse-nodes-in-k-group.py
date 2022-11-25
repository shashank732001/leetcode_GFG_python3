# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return none
        
        prev = None
        temp = None
        curr = head
        count = 0
        
        while curr and  count<k:
            temp = curr.next
            curr.next = prev
            prev,curr = curr,temp
            count+=1
        
        if temp:
            curr1 = temp
            count = 0
            while curr1 and count<k:
                curr1 = curr1.next
                count+=1
            if count==k:    
                
                head.next = self.reverseKGroup(temp,k)
            else:
                head.next = temp
        
        return prev
        