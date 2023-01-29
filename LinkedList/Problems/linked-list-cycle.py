class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        
        fast = slow = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False

    """
    Naive Solution 
    Using HAshMap's to store the node's next value
    """
    def hasCycle_Naive(self, head) -> bool:
        if head is None or head.next is None:
            return False

        check = dict()
        while head:
            if head.next in check:
                return True 
            check[head.next] = 1 
            head = head.next
        return False