
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        stack = []

        for i, c in enumerate(s):
            if '(' == c:
                stack.append((i, c))
            elif ')' == c:
                if len(stack) == 0:
                    stack.append((i, c))
                    continue

                prev = stack[-1]
                if prev[1] == '(':
                    stack.pop()

                    if i + 1 == len(s):
                        stack.append((i + 1, c))
                else:
                    stack.append((i, c))

        cnt_stack = len(stack)
        if cnt_stack < 1:
            return len(s)

        max_step = stack[0][0]
        for i in range(1, cnt_stack):
            max_step = max(max_step, stack[i][0] - stack[i - 1][0] - 1)

        return max_step


if __name__ == "__main__":
    print Solution().longestValidParentheses(")()())")
    print Solution().longestValidParentheses(")()")
    print Solution().longestValidParentheses("()")
    print Solution().longestValidParentheses("())")
