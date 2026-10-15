# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        faster = head

        while faster and faster.next:
            slow = slow.next
            faster = faster.next.next

            if slow == faster:
                return True
        return False
            