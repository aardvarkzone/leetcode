# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        head_start = ListNode()
        head_start.next = head.next
        curr = head
        prev = None

        while curr and curr.next: 
            second = curr.next
            first = curr
            temp = curr.next.next
            if prev: prev.next = second
            second.next = first
            first.next = temp
            curr = first.next
            prev = first

        return head_start.next
