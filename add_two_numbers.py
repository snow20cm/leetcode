# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lr_head = ListNode(0)
        lr_end = lr_head
        carry_bit = 0

        while l1 or l2:
            l1v = 0 if l1 is None else l1.val
            l2v = 0 if l2 is None else l2.val
            sum = l1v + l2v + carry_bit
            carry_bit = 0 if sum < 10 else 1
            lr_end.next = ListNode(sum if sum < 10 else sum - 10)
            lr_end = lr_end.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry_bit is 1:
            lr_end.next = ListNode(1)

        return lr_head.next


s = Solution()
l1 = l1_tail = ListNode(0)
l1_tail.next = ListNode(3)
l1_tail = l1_tail.next
l1_tail.next = ListNode(8)
l1_tail = l1_tail.next
l1_tail.next = ListNode(1)
l1_tail = l1_tail.next

l2 = l2_tail = ListNode(0)
l2_tail.next = ListNode(3)
l2_tail = l2_tail.next
l2_tail.next = ListNode(8)
l2_tail = l2_tail.next
l2_tail.next = ListNode(9)
l2_tail = l2_tail.next


lr = s.addTwoNumbers(l1, l2)

while(lr):
    print(lr.val, end = '')
    lr = lr.next
