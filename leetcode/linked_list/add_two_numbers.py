# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        index_l1, index_l2 = l1, l2
        resultant = None
        while (index_l1 and index_l2):
            sum = index_l1.val + index_l2.val + carry
            if not resultant:
                resultant = ListNode(sum%10)
                head = resultant
            else:
                head.next = ListNode(sum%10)
                head = head.next
            carry = sum//10
            index_l1, index_l2 = index_l1.next, index_l2.next
        while(index_l1):
            sum = index_l1.val + carry
            head.next = ListNode(sum%10)
            head, carry, index_l1 = head.next, sum//10, index_l1.next
        while(index_l2):
            sum = index_l2.val + carry
            head.next = ListNode(sum%10)
            head, carry, index_l2 = head.next, sum//10, index_l2.next
        if carry: head.next = ListNode(carry)
        return resultant