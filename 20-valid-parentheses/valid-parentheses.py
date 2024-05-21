class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                if not stack or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True
