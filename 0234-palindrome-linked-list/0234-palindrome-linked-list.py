# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
            
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Compare the first half and the reversed second half
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed second half
        
        while second_half:  # We only need to check until the end of the second half
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
            
        return True
