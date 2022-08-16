// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # Get the left part correct
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
            
        # Middle part, reverse and iterate r-l+1 times
        prev = None
        for i in range(right - left + 1):
            next_copy = cur.next
            cur.next = prev
            prev, cur = cur, next_copy
        # Connecting parts together
        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next