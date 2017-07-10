
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if not head:
            return None
            
        phead = head
        next = head.next
        dup = False
        
        while head:
            if next:
                if head.val == next.val:
                    next = next.next
                    dup = True
                else:
                    if dup:
                        head.val = next.val
                        head.next = next.next
                        next = next.next
                        dup = False
                    else:
                        head = head.next
                        next = next.next
            else:
                if dup:
                    head = None
                else:
                    head.next = next
                    head = next
                        
        return phead
