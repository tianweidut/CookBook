#coding: utf-8

PATH_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
}

def chk(input):
    stack = []

    for i in input:
        if i in ('(', '[', '{'):
            stack.append(i)
        elif i in (')', ']', '}'):
            if len(stack) == 0 or stack.pop() != PATH_MAP.get(i):
                return False

    return len(stack) == 0

if __name__ == "__main__":
    inputs = [
        "()(()){([()])}",
        "((()(()){([()])}))",
        ")(()){([()])}",
        "({[])}",
        "("
    ]

    for i in inputs:
        print(i, chk(i))