# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr_node = dummy
        
        if not head:return None
        
        while curr_node.next:
            if curr_node.next.val == val:
                curr_node.next =curr_node.next.next

            else:
                curr_node = curr_node.next
        return dummy.next    