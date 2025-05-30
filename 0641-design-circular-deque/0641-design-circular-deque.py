class MyCircularDeque:

    def __init__(self, k: int):
        self.deq = deque()
        self.k = k
    def insertFront(self, value: int) -> bool:
        if len(self.deq) >= self.k:
            return False

        self.deq.appendleft(value)
        return True
        
    def insertLast(self, value: int) -> bool:
        if len(self.deq) >= self.k:
            return False

        self.deq.append(value)
        return True      

    def deleteFront(self) -> bool:
        if self.deq:
            self.deq.popleft()
            return True
        
        return False

    def deleteLast(self) -> bool:
        if self.deq:
            self.deq.pop()
            return True
        
        return False    

    def getFront(self) -> int:
        if self.deq:
            return self.deq[0]
        
        return -1

    def getRear(self) -> int:
        if self.deq:
            return self.deq[-1]
        
        return -1        

    def isEmpty(self) -> bool:
        if self.deq:
            return False
        
        return True

    def isFull(self) -> bool:
        if len(self.deq) >= self.k:
            return True
        
        return False        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()