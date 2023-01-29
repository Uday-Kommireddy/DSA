from linkedlist import Node

"""
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.
"""
class Solution:
    """
    Leetcode Discussion for further reference:
    https://leetcode.com/problems/remove-linked-list-elements/solutions/1572935/python-99-one-pass-solution-with-explanation/
    """
    def removeElements(self, head, val):
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else: 
                    head = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return head
    
    """
    In the Naive solution, we ought to create a new LinkedList from the given head. 
    """
    def removeElements_Naive(self, head, val):
        dummy_head = Node(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next
