# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carryval = 0
        
        while l1 or l2:
            d = carryval
            if l1 and l2:
                d += (l1.val+l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                d += (l1.val)
                l1 = l1.next
            elif l2:
                d += (l2.val)
                l2 = l2.next
            carryval = d // 10
            cur.next = ListNode(d%10)
            cur = cur.next
        if carryval == 1: cur.next = ListNode(1)
        return dummy.next
                