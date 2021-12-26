# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: min(self.val, other.val)
        dummy = dummy_tail = ListNode(-1)
        h = []
        for internal_list in lists:
            if internal_list:
                heapq.heappush(h, (internal_list.val, internal_list))
            
        while any(h):
            node = heapq.heappop(h)[1]
            dummy_tail.next = node
            dummy_tail = dummy_tail.next
            if node.next:
                node = node.next
                heapq.heappush(h, (node.val, node))
        return dummy.next
