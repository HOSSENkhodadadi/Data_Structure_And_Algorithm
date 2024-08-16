from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currentL1 = l1
        currentL2 = l2
        num1 = 0
        num2 = 0
        i = 1
        while currentL1: 
            num1 += currentL1.val * i 
            currentL1 = currentL1.next
            i *= 10
        i = 1
        while currentL2:
            num2 += currentL2.val * i
            currentL2 = currentL2.next
            i *= 10    
        num = num1 + num2 
        head = ListNode(num % 10)
        num = num // 10
        current = head 
        while num != 0:
            current.next = ListNode(num % 10)
            current = current.next
            num = num // 10
        return head
        
# # creates a linked list using regular list
# test_list = [1, 2, 3]
# head = ListNode(test_list[0])
# lList = head
# for i in range(1,len(test_list) ):
#     lList.next = ListNode(test_list[i])
#     lList = lList.next
# prints it down
# current = head
# while current:
#     print(current.val)
#     current = current.next
        