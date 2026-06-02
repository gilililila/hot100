from typing import Optional
from p7_ultils import getList, printList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ explanation
        要删除倒数第 n 个节点，需要找到倒数第 n+1 个节点，
        可以先让第一个指针走 n 步，然后两个指针同时走，等第一个指针到达末尾时，第二个指针位于倒数 n+1 个节点
        考虑到可能会要求删除链表的头节点，n == len(list)，头部增加一个哨兵节点，放置越界
        """
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

test_cases = [
    [[1,2,3,4,5],2],
    [[1],1],
    [[1,2],1]
]

for case in test_cases:
    s = Solution()
    head = getList(case[0])
    s.removeNthFromEnd(head, case[1])
    printList(head)
