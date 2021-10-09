# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        aval = ListNode(val=None)
        while head != None:
            if head.val == aval.val:
                aval.next = head.next
            else:
                aval = head
            head = head.next
        return first
        # Gatito azuloso

# EOF #
