# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list2==None:
            return list1
        else:
            temp=list2
        while list1!=None:
            if temp.val>list1.val:
                if list2==temp:
                    t=list1.next
                    list1.next=temp
                    list2=list1
                    list1=t
                else:
                    te=list2
                    while te.next!=temp:
                        te=te.next
                    t=list1.next
                    te.next=list1
                    te.next.next=temp
                    list1=t
            elif temp.next!=None:
                temp=temp.next
            else:
                t=list1.next
                list1.next=None
                temp.next=list1
                list1=t
        return list2
            
        
        