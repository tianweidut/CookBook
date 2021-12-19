class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pop_stack = []
        self.push_stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())  

        return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        x = self.pop()
        self.pop_stack.append(x)
        return x



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.pop_stack) == 0 and len(self.push_stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()