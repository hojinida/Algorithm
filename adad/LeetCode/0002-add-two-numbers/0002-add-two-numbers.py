# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =ListNode()
        addPlus =0 

        pointer = dummy
        lastPointer = dummy
        while l1 or l2 or addPlus > 0:
            s = addPlus
            if l1:
                s+=l1.val
                l1= l1.next
            if l2:
                s+=l2.val
                l2 = l2.next
            if s > 9:
                s -= 10
                addPlus=1
            else:
                addPlus = 0
            lastPointer = pointer
            pointer.val = s
            pointer.next = ListNode()
            pointer = pointer.next
        lastPointer.next=None
        return dummy