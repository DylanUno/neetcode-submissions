# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        container = []

        while curr:
            container.append(curr)
            curr = curr.next
        
        i = 0
        j = len(container) - 1
        reordered = container[0]

        while i < j:
            container[i].next = container[j]
            i += 1
            if i == j:
                break
            
            container[j].next = container[i]
            j -= 1
        
        container[i].next = None
        

        