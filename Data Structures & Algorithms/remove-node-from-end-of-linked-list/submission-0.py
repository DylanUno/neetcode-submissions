# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        index1 = head
        index2 = dummy

        for i in range(n):
            index1 = index1.next
        
        while index1:
            index1 = index1.next
            index2 = index2.next

        index2.next = index2.next.next
    

        return dummy.next

        