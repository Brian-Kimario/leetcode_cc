# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        # Handle edge cases where list has 0, 1, or 2 nodes
        if not head or not head.next:
            return head
        
        odd = head          # Tracks the tail of the odd list
        even = head.next    # Tracks the tail of the even list
        even_head = even    # Saves the start of even list to connect later
        
        # Traverse until there are no more even nodes to process
        while even and even.next:
            odd.next = even.next  # Link current odd node to next odd node
            odd = odd.next        # Move odd pointer forward
            
            even.next = odd.next  # Link current even node to next even node
            even = even.next      # Move even pointer forward
            
        odd.next = even_head      # Connect the end of odd list to head of even list
        
        return head