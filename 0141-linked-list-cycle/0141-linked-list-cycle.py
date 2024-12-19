# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pattern = {}
        while head:
            if head in pattern:
                return True
            else:
                pattern[head] = 1
            
            head=head.next

        return False