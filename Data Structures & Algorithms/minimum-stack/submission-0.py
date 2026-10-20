class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack[val] = self.min_stack.get(val, 0) + 1
        
    def pop(self) -> None:
        curr_pop = self.top()
        self.stack.pop(-1)
        self.min_stack[curr_pop] -=1
        if self.min_stack[curr_pop] == 0:
            del self.min_stack[curr_pop]
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.min_stack.keys())
        
        
