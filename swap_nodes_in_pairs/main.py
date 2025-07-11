from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        is_swapping = True
        curr = head

        while curr:
            if is_swapping and curr.next:
                print("swapping")
                start = curr
                second = curr.next
                rest = curr.next.next
                start.next = rest
                second.next = start
                curr = second

            is_swapping = not is_swapping
            curr = curr.next

        while head:
            print(head.val)
            head = head.next

        return head


solution = Solution()
print(solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
print(solution.swapPairs(ListNode(1, ListNode(2, ListNode(3)))))
