class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0 and len(popped) == 0:
            return True
        
        if len(pushed) == 0 or len(popped) == 0:
            return False
        
        stack = [pushed[0]]
        i = 1
        j = 0
        
        while j < len(popped):
            if len(stack) !=0 and popped[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                if i < len(pushed):
                    stack.append(pushed[i])
                    i += 1
                else:
                    return False
                
        return True
            
        