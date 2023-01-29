"""
Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
"""

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head

        current = head 
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next 
            else:
                current = current.next 
        
        return head