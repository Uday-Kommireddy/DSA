"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
"""
class Solution:
    def reverse_linked_list(self, node):
        if node is None or node.next is None:
            return node 
        
        to_next = previous = None

        while node:
            to_next = node.next
            node.next = previous
            previous = node
            node = to_next
        
        return previous

    def middle_of_linked_list(self, node):
        if node is None or node.next is None:
            return node
        
        fast = slow = node
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 

            if fast == None:
                break
        
        return slow

    def isPalindrome(self, head)-> bool:
        if head is None: 
            return False
        
        if head.next is None:
            return True
        
        middle_pointer = self.middle_of_linked_list(head)

        reversed_middle_node = self.reverse_linked_list(middle_pointer)

        while head and reversed_middle_node:
            if reversed_middle_node.val != head.val:
                return False
            
            reversed_middle_node = reversed_middle_node.next
            head = head.next 
        
        return True
    """
    Just store the values in a list, check if list == list[::-1]s
    """
    def isPalindrome_Naive(self, head) -> bool:
        if not head or not head.next:
            return True 
        
        values = list()
        while head:
            values.append(head.val)
            head = head.next 
        
        return values == values[::-1]
