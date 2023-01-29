"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

class Solution:
    def middleNode(self, head):
        if not head or not head.next:
            return head

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    """
    Naive Method
    Just store the nodes in a list,
    return the middle of the list
    """

    def middleNode_Naive(self, head):
        if head is None or head.next is None:
            return head 
        
        nodes = list()
        while head:
            nodes.append(head)
            head = head.next 
        
        return nodes[len(nodes)//2]
