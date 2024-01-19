# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        h2 = slow.next
        tail = slow.next = None
        while h2:
            temp = h2.next
            h2.next = tail
            tail = h2
            h2 = temp

        # merge two halfs
        h1, h2 = head, tail
        while h2:
            temp1, temp2 = h1.next, h2.next
            h1.next = h2
            h2.next = temp1
            h1, h2 = temp1, temp2