# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while True:
            if head != None:
                if head.val == val:
                    head = head.next
                else:
                    break
            else:
                return head
        last = head
        actual = head.next
        while actual != None:
            if actual.val == val:
                last.next = actual.next
            else:
                last = actual
            actual = actual.next
        return head

# EOF #
