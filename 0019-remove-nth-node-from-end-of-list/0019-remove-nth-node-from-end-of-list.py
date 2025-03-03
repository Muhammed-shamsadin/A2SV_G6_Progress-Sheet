# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
            1 -> 2 -> 3 -> 4 -> 5
        '''
        dummy = ListNode()
        dummy.next = head

        # determine the length of the ListNode by iterating through the whole ListNode
        counter = 0
        itr = head
        while itr:
            counter += 1
            itr = itr.next
        
        # get the nth index from beginning
        remove_idx = counter - n

        # iterate and remove the remove_idx
        i = 0
        ptr = head
        prev = dummy
        while ptr:
            if i == remove_idx:
                prev.next = ptr.next

            ptr = ptr.next
            prev = prev.next
            i += 1
        
        return dummy.next
        