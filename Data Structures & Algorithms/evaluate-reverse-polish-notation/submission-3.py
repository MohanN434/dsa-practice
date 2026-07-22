class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sumStack = []
        ops = {"+": self.add, "-": self.sub, "*": self.mul, "/": self.div}

        for token in tokens:
            if token in ops:
                op2 = sumStack.pop()
                op1 = sumStack.pop()
                sumStack.append(ops[token](op1, op2))
            else:
                sumStack.append(int(token))

        return sumStack[-1]

    def add(self, op1: int, op2: int) -> int:
        return op1 + op2
    
    def sub(self, op1: int, op2: int) -> int:
        return op1 - op2
    
    def mul(self, op1: int, op2: int) -> int:
        return op1 * op2
    
    def div(self, op1: int, op2: int) -> int:
        return int(op1 / op2)
                

