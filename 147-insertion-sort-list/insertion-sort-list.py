class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            next_node = curr.next

            # Find correct position
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr
            curr.next = prev.next
            prev.next = curr

            curr = next_node

        return dummy.next