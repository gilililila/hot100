from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
