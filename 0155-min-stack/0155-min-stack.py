class MinStack:

    def __init__(self):
        
        self._list =[]
        self._top = -1
        

    def push(self, val: int) -> None:
        self._list.append(val)
        self._top+=1
        
        

    def pop(self) -> None:
        self._list.pop()
        self._top-=1
        

    def top(self) -> int:
        return self._list[self._top]
        

    def getMin(self) -> int:
        return min(self._list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()