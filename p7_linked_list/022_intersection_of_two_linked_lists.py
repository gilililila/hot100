from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


"""
test_cases = [
    [listA, listB, intersectVal]
]
"""
test_cases = [
    [[4,1,8,4,5],[5,6,1,8,4,5],8],
    [[1,9,1,2,4],[3,2,4],2],
    [[2,6,4],[1,5],0],
]
