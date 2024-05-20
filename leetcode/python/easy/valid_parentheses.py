"""
constraints
--
valid parentheses: '(', ')', '{', '}', '[' and ']'
1 <= s.length <= 10**4
s consists of parentheses only '()[]{}'.

pseudocode
--
stack = []

for char in s:
    if char in ["(", "{", "["]:
        append char to stack
    else:
        if char == ")":
            latest_in_stack = stack.getLatestElement()
            if latest_in_stack != "(":
                return false
        elif char == "}":
            latest_in_stack = stack.getLatestElement()
            if latest_in_stack != "{":
                return false
        elif char == "]":
            latest_in_stack = stack.getLatestElement()
            if latest_in_stack != "[":
                return false
return true
"""
import random


def isValid(s: str) -> bool:
    if len(s) < 1 or len(s) > 10 ** 4:
        raise RuntimeError("String length out of bounds")

    stack = []

    if len(s) % 2 != 0:
        return False

    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            try:
                if char == ")":
                    if stack.pop() != "(":
                        return False
                elif char == "}":
                    if stack.pop() != "{":
                        return False
                elif char == "]":
                    if stack.pop() != "[":
                        return False
                else:
                    return False
            except IndexError:
                return False
    return True if len(stack) == 0 else False


if __name__ == "__main__":
    # print(isValid("{}[()"))
    # print(isValid("()[]{}"))
    # print(isValid("(]"))

    while True:
        a = "".join(random.sample(population=['(', ')', '{', '}', '[', ']'], k=5))
        print(len(a))
        print(a)
        print(isValid(a))

        if isValid(a):
            print("Match")
            break
