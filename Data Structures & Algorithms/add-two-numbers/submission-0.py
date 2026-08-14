class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # res acts as a 'dummy' head to anchor the list
        res = ListNode(0)
        current = res
        carry = 0

        # We continue as long as there are digits left in either list OR a leftover carry
        while l1 or l2 or carry:
            # Get values from nodes, or 0 if we've reached the end of a list
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10

            # 1. Create the new node and ATTACH it to the list
            current.next = ListNode(val)
            
            # 2. Move 'current' forward to the node we just created
            current = current.next

            # Move input pointers forward if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Return the list starting AFTER the dummy node
        return res.next