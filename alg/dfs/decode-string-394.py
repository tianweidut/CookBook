
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        cnt_stack = []
        s_stack = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                i += 1
                while s[i] != '[':
                    i += 1
                cnt_stack.append(int(s[start:i]))
                i -= 1
            elif s[i] == ']':
                tmp = ""
                cur = s_stack.pop()
                while cur != '[':
                    tmp = cur + tmp

                    if len(s_stack) > 0:
                        cur = s_stack.pop()
                    else:
                        break
                s_stack.append(cnt_stack.pop() * tmp)
            else:
                s_stack.append(s[i])
            i += 1

        return "".join(s_stack)


if __name__ == "__main__":
    print Solution().decodeString("3[a]2[bc]")
    print Solution().decodeString("3[a2[c]]")
    print Solution().decodeString("2[abc]3[cd]ef")
