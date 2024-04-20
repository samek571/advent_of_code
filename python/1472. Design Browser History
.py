class BrowserHistory:

    def __init__(self, homepage: str):
        self.stck=[homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.stck = self.stck[:self.pointer+1]
        self.stck.append(url)
        self.pointer+=1

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer-steps)
        return self.stck[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(self.pointer+steps, len(self.stck)-1)
        return self.stck[self.pointer]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
