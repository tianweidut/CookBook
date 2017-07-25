
class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if not stack or c in ('(', '{', '['):
                stack.append(c)
            else:
                top = stack[-1]
                if ((top == '{' and c == '}') or
                        (top == '[' and c == ']') or
                        (top == '(' and c == ')')):
                    stack.pop()
                else:
                    return False

        return not bool(stack)
