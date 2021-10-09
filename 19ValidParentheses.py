class Solution:
    def isValid(self, s: str) -> bool:
        delims = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []

        for char in s:
            if char in delims.keys():
                stack.append(delims[char])
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == char:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0

# EOF #
