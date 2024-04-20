class MyQueue:

    def __init__(self):
        self.stack = []
        self.hlpr = []

    def push(self, x: int) -> None:
        while len(self.stack):
            self.hlpr.append(self.stack.pop())

        self.stack.append(x)

        while len(self.hlpr):
            self.stack.append(self.hlpr.pop())


    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not len(self.stack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()