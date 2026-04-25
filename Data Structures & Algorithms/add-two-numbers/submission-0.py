# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1.val
        num2 = l2.val

        while l1.next:
            l1 = l1.next
            num1 = (num1 * 10) + l1.val
        
        while l2.next:
            l2 = l2.next
            num2 = (num2 * 10) + l2.val

        summ = int(str(num1)[::-1]) + int(str(num2)[::-1])

        summ = str(summ)[::-1]

        dummy = ListNode(0)
        tail = dummy
        for num in summ:
            tail.next = ListNode(num)
            tail = tail.next

        return dummy.next