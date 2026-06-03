from Scripts.activate_this import prev_length

from p7_ultils import getList, printList, ListNode
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ explanation
        每次交换后，交换的头节点会与后一节点换位，头节点会改变，注意更新头节点
        """
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = cur
            prev.next = temp

            prev = cur
            cur = cur.next
        return dummy.next

    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            temp = cur.next
            post = temp.next

            prev.next = temp  # 0->2
            temp.next = cur  # 2->1
            cur.next = post  # 1->3

            # next turn
            prev = cur
            cur = post
        return dummy.next


test_cases = [
    [1,2,3,4],
    [],
    [1]
]

for case in test_cases:
    s = Solution()
    head = getList(case)
    s.swapPairs(head)
    printList(head)
