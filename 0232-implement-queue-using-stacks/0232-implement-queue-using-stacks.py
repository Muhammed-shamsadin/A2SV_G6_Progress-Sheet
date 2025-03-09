class MyQueue:

    def __init__(self):
        self.index = 0
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        popped = self.stack[self.index]
        self.index += 1

        return popped

    def peek(self) -> int:

        return self.stack[self.index]
    

    def empty(self) -> bool:
        return self.index == len(self.stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()