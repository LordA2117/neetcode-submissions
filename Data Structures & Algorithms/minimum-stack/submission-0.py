class MinStack:

    def __init__(self):
        self.array = []
        

    def push(self, val: int) -> None:
        self.array.append(val)
        

    def pop(self) -> None:
        self.array.pop()
        

    def top(self) -> int:
        if self.array != []:
            return self.array[-1]
        

    def getMin(self) -> int:
        if self.array:
            return min(self.array)
        
