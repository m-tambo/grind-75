# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()    # create a dummy node for the head of the list
        curr = head          # make a marker node which becomes the new linked list

        while list1 and list2:
            if list1 < list2:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next
            
            curr = curr.next
        
        curr = list1 if list1 else list2
        return head.next
