from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ explanation
        floyd 判圈算法
        假设头节点走到入环口需要 a 步，假设环长为 c
        在 slow 与 fast 时，假设 slow 走了 b，则 fast 走了 2b 步
        假设快指针比慢指针多走了 k 圈，则 2b-b = kc => b = kc
        慢指针从入环口开始，在环中走了 b-a = kc-a 步相遇了，说明从相遇点开始，再走 a 步就恰好走到入环口
        未知 a，但是如果此时让一个指针从头开始，与慢指针同时走，
        恰好 a 步后二者必定相遇，且相遇点在入环口。这个指针就是如环的第一个节点
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head
        return None