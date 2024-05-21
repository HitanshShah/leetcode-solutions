# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 and list2:
        #     head = ListNode()
        #     if(list1.val >= list2.val):
        #         head.val = list2.val
        #         head.next = self.mergeTwoLists(list1, list2.next)
        #     else:
        #         head.val = list1.val
        #         head.next = self.mergeTwoLists(list1.next, list2)
        #     return head
        # elif list1 and not list2:
        #     return list1
        # elif list2 and not list1:
        #     return list2
        # else:
        #     return None
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return head.next