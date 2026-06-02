from typing import Optional
from p7_ultils import getList, printList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

test_cases = [
    [[1,2,4],[1,3,4]],
    [[],[]],
    [[],[0]]
]

for case in test_cases:
    s = Solution()
    list1 = getList(case[0])
    list2 = getList(case[1])
    res = s.mergeTwoLists(list1, list2)
    printList(res)
