# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_table = {}
        
        curr = head
        while curr:
            if curr in hash_table:
                return True
            else:
                hash_table[curr] = 0
            curr = curr.next
        
        return False
