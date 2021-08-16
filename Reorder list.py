
    def _getMiddleNode(self, head: ListNode) -> (ListNode, ListNode):
        slow = head
        before_slow = head
        fast = head
        fast_only = False
        while fast.next:
            fast = fast.next
            if not fast_only:
                before_slow = slow
                slow = slow.next
            fast_only = not fast_only
        return slow, before_slow

    def _reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def _mergeEqualLists(self, head1: ListNode, head2: ListNode):
        if head1 == head2:
            return
        
        curr1 = head1
        curr2 = head2

        while curr1 and curr2:
            n1 = curr1.next
            n2 = curr2.next
            curr1.next = curr2
            if n1:
                curr2.next = n1
            curr1 = n1
            curr2 = n2
                

    def reorderList(self, head: Optional[ListNode]) -> None:
       
        if not head:
            return
