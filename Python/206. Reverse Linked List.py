# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nex, pre = head, None
        while nex :
            tmp =  nex.next
            nex.next = pre
            pre = nex
            nex = tmp
        return  pre
