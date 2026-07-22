class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(ops[token](op1, op2))
            else:
                stack.append(int(token))

        return stack.pop()

