# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        if not curr1 or not curr2:
            return None
        while curr1 or curr2:
            
            if curr1 == curr2:
                return curr1
            
            if not curr1:
                curr1 = headB
            else:    
                curr1 = curr1.next
                
            if not curr2:
                curr2 = headA
            else:
                curr2 = curr2.next
        return None        