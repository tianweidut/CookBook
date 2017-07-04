

class MinStack(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, number):
        self.s1.append(number)
        if self.s2:
            number = min(self.s2[-1], number)
        self.s2.append(number)

    def pop(self):
        if not self.s1:
            return None

        self.s2.pop()
        return self.s1.pop()

    def min(self):
        if not self.s2:
            return None

        return self.s2[-1]
