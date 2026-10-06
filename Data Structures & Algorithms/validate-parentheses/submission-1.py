class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")":"(","]":"[","}":"{"}
        stack = []

        for c in s:  
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    # if doesn't match because the stack is empty
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
            