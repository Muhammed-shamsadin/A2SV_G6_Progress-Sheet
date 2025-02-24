class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        counter = 0
        itr = self.head
        while itr and counter < index:
            itr = itr.next
            counter += 1

        return itr.val if itr else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        counter = 0
        itr = self.head
        while itr and counter < index - 1:
            itr = itr.next
            counter += 1

        if itr:
            new_node = Node(val, itr.next)
            itr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        counter = 0
        itr = self.head
        while itr and counter < index - 1:
            itr = itr.next
            counter += 1

        if itr and itr.next:
            itr.next = itr.next.next

