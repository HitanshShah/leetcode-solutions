class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            elif char == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif char == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif char == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        return stack.pop()