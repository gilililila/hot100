from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ explanation
        快慢指针，慢指针走一步，快指针走两步。若链表有环，快指针终将会再次追赶上慢指针。
        快指针变为 None 时，链表结束，说明没有环
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

"""
pos => 表示链表尾连接到链表中的位置, -1 表示链表中没有环
test_cases = [
    [head, pos]
]
"""
test_cases = [
    [[3,2,0,-4], 1],
    [[1,2], 0],
    [[1], -1],
    [[1,2], -1]
]