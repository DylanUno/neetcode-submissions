# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            current1 = list1.next
            current2 = list2
        else:
            head = list2
            current1 = list1
            current2 = list2.next
        
        curr = head

        while current1 and current2:
            if current1.val <= current2.val:
                curr.next = current1
                current1 = current1.next
            else:
                curr.next = current2
                current2 = current2.next
            
            curr = curr.next
        
        if current1:
            curr.next = current1
        elif current2:
            curr.next = current2

        
        return head