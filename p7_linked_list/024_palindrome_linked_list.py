from typing import Optional
from p7_ultils import ListNode, getList, printList

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """ explanation
        将链表值记录到列表中，比较列表反转是否相同
        时间复杂度 O(n)
        空间复杂度 O(n)
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        if nums == nums[::-1]:
            return True
        return False

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def revList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        """ explanation
        判断链表是否回环，需要比较链表 前半部分 和 后半部分反转 是否相同
        构造两个辅助函数，
            获取链表中点的函数，快指针比慢指针快两步，当快指针跳到None时，慢指针刚好位于中点或右半部分起点
            反转链表函数，利用头插法不断将curNode下一个元素插入，达到反转效果。
        遍历 反转后的链表 与 原链表，比较其值，注意反转后链表一定比原链表先结束，所以判断条件为反转后链表
        """
        mid = self.getMid(head)
        head2 = self.revList(mid)
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

test_cases = [
    [1,2,3,5,3,2,1],
    [1,2,2,1],
    [1,2]
]

for case in test_cases:
    s = Solution()
    head = getList(case)
    printList(head)
    print(s.isPalindrome1(head))
