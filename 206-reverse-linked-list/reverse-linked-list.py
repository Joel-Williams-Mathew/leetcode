class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None
        current = head

        while current:

            nextNode = current.next

            current.next = previous

            previous = current

            current = nextNode

        return previous