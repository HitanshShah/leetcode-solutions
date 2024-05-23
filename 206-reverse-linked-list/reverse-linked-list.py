# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        while current.next:
            tempnode = current.next
            current.next = tempnode.next
            tempnode.next = head
            head = tempnode
            print(head.val)
        return head