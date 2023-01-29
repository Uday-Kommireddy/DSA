"""
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Reversing Processing, 

While iterating
1) store the next pointer of head, ahead.
2) As reversing, head of cuurent will be previous. so head.next = previous
3) Update the previous to head,
4) Move the head to pointer stored in 1) .
"""
class Solution:
    def reverseList(self, head):
        #Edge case
        if head is None or head.next is None: return head

        previous = next_pointer = None

        while head:
            next_pointer = head.next
            head.next = previous
            previous = head
            head = next_pointer
        
        return previous