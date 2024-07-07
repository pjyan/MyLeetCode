# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pseudo = ListNode(0, head)
        cur = pseudo
        while cur.next and cur.next.next:
            tmp = cur.next.next.next
            tmp2 = cur.next
            cur.next =  cur.next.next
            cur.next.next = tmp2
            tmp2.next = tmp
            cur = cur.next.next
        return pseudo.next
