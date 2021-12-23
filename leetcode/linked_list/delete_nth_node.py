# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        fast = slow = dummy_head
        fast_ind = slow_ind = 0
        while fast_ind < n:
            fast = fast.next
            fast_ind += 1
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            
        if slow.next != head:
            slow.next = slow.next.next
        else:
            head = head.next
        return head
