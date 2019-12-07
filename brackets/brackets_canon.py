def solution(brackets):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for c in brackets:
        if c in "{[(":
            stack.append(c)
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0