from typing import Optional
from p7_ultils import getList, printList
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carrying = 0
        cur = dummy = ListNode()
        while l1 or l2 or carrying:
            num = carrying
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            cur.next = ListNode(num % 10)
            carrying = num // 10
            cur = cur.next
        return dummy.next

test_cases = [
    [[2,4,3],[5,6,4]],
    [[0],[0]],
    [[9,9,9,9,9,9,9],[9,9,9,9]]
]

for case in test_cases:
    s = Solution()
    l1 = getList(case[0])
    l2 = getList(case[1])
    res = s.addTwoNumbers(l1, l2)
    printList(res)
