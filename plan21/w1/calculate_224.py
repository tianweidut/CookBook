from collections import deque

# 使用deque双端队列替代list，deque可以在append和pop时候提供O(1)的复杂度，而list则需要O(n)的移动

class Solution:
    def calculate(self, s: str) -> int:
        return self._do_calculate(deque(s))
        
    
    def _do_calculate(self, s):
        sign = '+'
        num = 0
        stack = []
        
        while len(s) > 0:
            c = s.popleft()
            
            if c.isdigit():
                num = 10 * num + int(c)

            if c == '(':
                num = self._do_calculate(s)
                
            if (c != ' ' and not c.isdigit()) or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-1 * num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                    
                num = 0
                sign = c
                    
            if c == ')':
                break
        
        return sum(stack)