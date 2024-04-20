class MyLinkedList:

    def __init__(self):
        self.stck= []

    def get(self, index: int) -> int:
        return -1 if index>=len(self.stck) else self.stck[index]

    def addAtHead(self, val: int) -> None:
        self.stck.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.stck.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index<len(self.stck): 
            self.stck = self.stck[:index] + [val] + self.stck[index:]
        elif index == len(self.stck):
            self.stck.append(val)

    def deleteAtIndex(self, index: int) -> None:
        if index<len(self.stck): self.stck.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
