from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        rev_head = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return rev_head

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        return prev

test_cases = [
    [1,2,3,4,5],
    [1,2],
    []
]

def getList(arr: List[int]) -> Optional[ListNode]:
    nodes = [ListNode(val) for val in arr]
    for i in range(len(arr)-1):
        nodes[i].next = nodes[i+1]
    head = nodes[0] if nodes else None
    return head

def printList(head: Optional[ListNode]) -> None:
    if head is None:
        return
    while head is not None:
        print(head.val, end="->")
        head = head.next
    print("End")

for case in test_cases:
    s = Solution()
    head = getList(case)
    res = s.reverseList2(head)
    printList(res)