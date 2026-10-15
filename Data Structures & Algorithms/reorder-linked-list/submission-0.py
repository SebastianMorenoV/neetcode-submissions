# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Create the new separate list 
        
        second = slow.next
        slow.next = None

        ## reverse the second half  
        prev = None
        curr = second
        while curr:
            ## invert the order.
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        ## once we have the second half inverted whe added like a zip
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1 

            first = tmp1
            second = tmp2
        


