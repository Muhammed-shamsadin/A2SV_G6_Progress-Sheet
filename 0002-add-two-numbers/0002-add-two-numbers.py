# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
         2 - 4 - 3 = 342
         5 - 6 - 4 = 465

                  
        '''
        temp = dummy = ListNode()

        if not l1:
            return l2
        elif not l2:
            return l1
        
        carry = 0
        while l1 and l2:
            node = ListNode()
            val = l1.val + l2.val + carry
            carry = val // 10
            val %= 10
            node.val = val
            temp.next = node

            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        
        while l1 and carry:
            node = ListNode()
            val = l1.val + carry
            carry = val // 10
            val %= 10
            node.val = val
            temp.next = node

            l1 = l1.next
            temp = temp.next
        
        while l2 and carry:
            node = ListNode()
            val = l2.val + carry
            carry = val // 10
            val %= 10
            node.val = val
            temp.next = node

            l2 = l2.next
            temp = temp.next

        
        if carry:
            node = ListNode()
            node.val = carry
            temp.next = node
        
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        
        return dummy.next
