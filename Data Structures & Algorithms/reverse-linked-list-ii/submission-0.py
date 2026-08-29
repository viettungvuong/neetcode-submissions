# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        before_left = dummy

        for _ in range(left - 1):
            before_left = before_left.next

        curr = before_left.next
        prev = None
        for _ in range(right - left + 1):
            move_to = curr.next
            curr.next = prev
            prev = curr
            curr = move_to

        before_left.next.next = curr  # curr đang ở vị trí (right + 1)
        before_left.next = prev       # prev đang ở vị trí right (giờ là đầu của đoạn đảo)

        return dummy.next
