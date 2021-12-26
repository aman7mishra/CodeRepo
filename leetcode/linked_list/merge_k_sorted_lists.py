# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: min(self.val, other.val)
        h = []
        head = tail = ListNode(0)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, lists[i]))
        while h:
            node = heapq.heappop(h)
            node = node[1]
            tail.next = node
            tail = tail.next
            if node.next:
                i+=1
                heapq.heappush(h, (node.next.val, node.next))
        return head.next
