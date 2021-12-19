
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        fake_head = ListNode(None, next=head)
        prev = fake_head

        while head:
            while head.next and head.val == head.next.val:
                head = head.next

            if prev.next == head:
                prev = head
            else:
                prev.next = head.next
            head = head.next
        return fake_head.next
