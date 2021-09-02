class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q1 = deque()
        self.q2 = deque() 

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            in_queue, out_queue = self.q2, self.q1
        else:
            in_queue, out_queue = self.q1, self.q2

        while len(out_queue) != 0:
            if len(out_queue) == 1:
                return out_queue.popleft()
            else:
                in_queue.append(out_queue.popleft())

    def top(self) -> int:
        """
        Get the top element.
        """
        x = self.pop()
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0 and len(self.q2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()