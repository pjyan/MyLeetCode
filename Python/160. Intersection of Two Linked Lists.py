# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a, len_b = 0, 0
        tempa, tempb = headA, headB
        while tempa:
            tempa = tempa.next
            len_a += 1         
        while tempb:
            tempb = tempb.next
            len_b += 1

        if len_a > len_b:
            tempa, tempb = headB, headA
            len_a, len_b = len_b, len_a
        else:
            tempa, tempb = headA, headB

        for _ in range(len_b - len_a):
            tempb = tempb.next
        
        while tempb:
            if tempb == tempa:
                return tempb
            tempa = tempa.next
            tempb = tempb.next
        
